N, x = map(int, input().split())
A = [0] + list(map(int, input().split()))
ans = 0
for i in range(N):
    if A[i] + A[i + 1] > x:
        tmp = A[i] + A[i + 1] - x
        ans += tmp
        A[i + 1] -= tmp
print(ans)
