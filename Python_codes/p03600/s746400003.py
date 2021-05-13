N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j] > A[i][k]+A[k][j]:
                print(-1)
                exit()

ans = 0
for i in range(N):
    for j in range(N):
        if all([A[i][j] < A[i][k]+A[k][j] or k==i or k==j for k in range(N)]):
            ans += A[i][j]
            
print(ans//2)
