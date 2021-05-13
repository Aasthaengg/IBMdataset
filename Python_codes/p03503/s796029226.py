N = int(input())
F = []
P = []
ans = -10**10
for i in range(N):
    F.append(list(map(int,input().split())))
for i in range(N):
    P.append(list(map(int,input().split())))
for i in range(1,2**10):
    profit = 0
    li = [0]*N
    for j in range(10):
        for k in range(N):
            if (i >> j & 1) and F[k][j]:
                li[k] += 1
    for k in range(N):
        profit += P[k][li[k]]
    ans = max(profit,ans)
print(ans)