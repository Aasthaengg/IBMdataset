import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

S = [0 for _ in range(N+1)]
for i in range(1, N+1):
    S[i] = S[i-1] + A[i-1]
# print(S)

ans = float("inf")
for i in range(0, N-1):
    ans = min(ans, abs((S[N] - S[i+1]) - (S[i+1] - S[0])))

print(ans)