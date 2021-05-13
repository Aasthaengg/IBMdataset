# C - Christmas Eve

N, K = map(int, input().split())
h = []
for _ in range(N):
    h.append(int(input()))

h.sort()
diffs = []
for i in range(K-1, N):
    diffs.append(h[i] - h[i-(K-1)])

print(min(diffs))