n,m,x = map(int, input().split())
C = [0]*n
A = []

for i in range(n):
    Q = list(map(int, input().split()))
    C[i] = Q[0]
    A.append(Q[1:])

ans = 10**7

for i in range(1 << n):
    res = True
    skill = [0]*m
    money = 0
    for j in range(n):
        if (i>>j)&1:
            for k in range(m):
                skill[k] += A[j][k]
            money += C[j]

    for s in skill:
        if s < x:
            res = False
    
    if res:
        ans = min(ans,money)

if ans == 10**7:
    print(-1)
else:
    print(ans)


