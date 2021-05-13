from collections import Counter
n = int(input())
count_list = []
for i in range(n):
    s = input()
    c = sorted(Counter(s).items(), key = lambda x:x[0])
    tmp = ""
    for j in range(len(c)):
        tmp += c[j][0]
        tmp += str(c[j][1])
    count_list.append(tmp)

c = Counter(count_list)
ans = 0
for i in c.values():
    if i >= 2:
        ans += i * (i - 1) // 2

print(ans)
