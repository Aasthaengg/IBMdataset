flag = True
n = int(input())
L = []
for i in range(n):
    t = int(input())
    L.append(t)
L.append(0)
if L[0] != 0:
    flag = False
cur = 0
ans = 0
for i in range(1, n+1):
    if cur < L[i]:
        if L[i]-cur != 1:
            flag = False
            break
        else:
            ans += 1
            cur = L[i]
    else:
        ans += L[i]
        cur = L[i]
if flag:
    print(ans)
else:
    print(-1)
