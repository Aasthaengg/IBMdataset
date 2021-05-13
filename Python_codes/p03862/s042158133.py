N, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for i in range(N-1):
    gap = A[i] + A[i+1] - x
    if gap > 0:
        ans += gap
        A[i+1] -= gap
        if A[i+1] < 0:
            A[i+1] = 0

print(ans)
