n = int(input())
A = list(map(int, input().split()))
L = [0] * n
for i in range(n-1):
    L[i+1] = 2 * A[i] - L[i]
ans = [0] * n
ans[0] = (A[-1] * 2 - L[-1]) // 2
for i in range(n-1):
    ans[i+1] = 2 * A[i] - ans[i]
print(*ans)
