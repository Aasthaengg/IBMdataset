N = int(input())
A = list(list(map(int, input().split())) for _ in range(2))
ans = 0
for i in range(N):
    ans = max(ans, sum(A[0][0:i+1])+sum(A[1][i:N]))
print(ans)