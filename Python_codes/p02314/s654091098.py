n, m = map(int, input().split())
C = list(map(int, input().split()))

N = [float('inf')] * (50000 + 1)
N[0] = 0
for i in range(1, 50000 + 1):
    for c in C:
        if i - c < 0:
            continue
        N[i] = min(N[i - c] + 1, N[i])

print(N[n])
