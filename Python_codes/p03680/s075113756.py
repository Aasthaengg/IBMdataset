n = int(input())

a = [int(input()) for _ in range(n)]

ans = 0
ind = 0
flag = 0
for i in range(n):
    t = a[ind]
    if t == 2:
        flag = 1
        ans += 1
        break
    else:
        ind = t-1
        ans += 1

if flag:
    print(ans)
else:
    print(-1)