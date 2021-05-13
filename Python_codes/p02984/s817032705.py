N = int(input())
A = list(map(int,input().split()))

SUM = sum(A)
tmp = 0
for i in range(1,N,2):
    tmp += A[i]
ans = [0]*N
ans[0] = SUM - 2*tmp
for i in range(1,N):
    ans[i] = 2*A[i-1] - ans[i-1]
print(*ans)