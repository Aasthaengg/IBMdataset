N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                exit()

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        for k in range(N):
            if k==i or k==j: continue
            if A[i][j] == A[i][k] + A[k][j]:
                break
        else:
            ans += A[i][j]
print(ans)