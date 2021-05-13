N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
need = [[True]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i==j or j==k or k==i:
                continue
            
            if A[i][j]+A[j][k]<A[i][k]:
                print(-1)
                exit()
                
            if A[i][j]+A[j][k]==A[i][k]:
                need[i][k] = False

ans = 0

for i in range(N):
    for j in range(N):
        if need[i][j]:
            ans += A[i][j]

print(ans//2)