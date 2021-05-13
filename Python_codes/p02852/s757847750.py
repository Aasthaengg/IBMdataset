n, m = map(int, input().split())
s = input()
ans = True
res = []
i = n
while i > 0:
    flag = 0
    for j in range(max(0, i - m), i):
        if s[j] == '0':
            flag = 1
            res.append(i - j)
            i = j
            break
    if flag == 0:
        ans = False
        break
if ans == False:
    print(-1)
else:
    for i in range(len(res) - 1, -1, -1):
        print(res[i])