N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
A.sort()
ans = 0
for i in range(len(A)):
    if A[i][1] >= M:
        ans += M*A[i][0]
        break
    ans += A[i][1]*A[i][0]
    M -= A[i][1]
print(ans)