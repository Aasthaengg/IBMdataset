N, K = map(int, input().split())
S = list(map(str, input()))

score = 0
for i in range(N - 1):
    if S[i + 1] == S[i]:
        score += 1
score = min(score + 2 * K, N - 1)

print(score)