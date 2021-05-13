N = int(input())
A = list(map(int, input().split()))

s = sum(A)
ans = float("inf")
cum = 0

for i in range(N-1):
    cum += A[i]
    ans = min(ans, abs(s - 2*cum))

print(ans)