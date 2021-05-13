N = int(input())
A = list(map(int, input().split()))
ans = [0 for i in range(N)]
x1 = sum(A)
for i in range(N):
    if i % 2 == 1:
        x1 -= 2 * A[i]
ans[0] = x1
for i in range(1, N):
    ans[i] = 2 * A[i-1] - ans[i-1]
print(*ans)