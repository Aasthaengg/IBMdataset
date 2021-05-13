N=int(input())
A=[list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans += A[i][j]

m = set()
for k in range(N):
    for i in range(N):
        if k==i: continue
        for j in range(i+1,N):
            if k==j: continue
            a = A[i][j]
            b = A[i][k] + A[k][j]
            if b == a: m.add((i,j))
            elif b < a:
                print(-1)
                exit()

for i,j in m:
    ans -= A[i][j]

print(ans)