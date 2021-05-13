n, k = map(int, input().split(" "))

a_dic = {}

a = list(map(int, input().split(" ")))
for i in a:
    if i in a_dic:
        a_dic[i] += 1
    else:
        a_dic[i] = 1

cn = 0
diff = len(a_dic) - k
score_sorted = sorted(a_dic.items(), key=lambda x:x[1], reverse=True)
if diff > 0:
    for i in range(diff):
        a = score_sorted.pop()
        cn += a[1]

print(cn)

