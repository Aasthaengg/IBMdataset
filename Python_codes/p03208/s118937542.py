N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort()

mini = 10 ** 9
for i in range(N - K + 1):
    mini = min(mini, abs(H[i] - H[i + K - 1]))

print(mini)
