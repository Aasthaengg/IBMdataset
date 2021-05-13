N, K = map(int, input().split())
total = 0
if not K:
    print(N ** 2)
    quit()

for b in range(K + 1, N + 1):
    total += (b - K) * (N // b) + max(0, N % b - K + 1)

print(total)
