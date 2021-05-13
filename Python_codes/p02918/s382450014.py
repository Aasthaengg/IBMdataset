# D - Face Produces Unhappiness

N, K = map(int, input().split())
S = str(input())

score = 0
for i in range(N - 1):
    if S[i] == S[i + 1]:
        score += 1

print(min(score + K * 2, N - 1))
