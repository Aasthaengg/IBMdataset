N = int(input())
A = list(map(int, input().split()))
sa = sum(A)
ans, min_diff = N, sa
for i in range(N - 1, -1, -1):
    d = abs(A[i] * N - sa)
    if d <= min_diff:
        ans = i
        min_diff = d
print(ans)