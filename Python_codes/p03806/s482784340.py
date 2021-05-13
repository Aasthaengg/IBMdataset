import sys
readlines = sys.stdin.buffer.readlines
input = sys.stdin.buffer.readline
N, Ma, Mb = map(int, input().split())
X = [tuple(map(int, line.split())) for line in readlines()]

INF = 1 << 30
x = [[INF]*201 for _ in [0]*201]
y = [[INF]*201 for _ in [0]*201]

n = N//2
X, Y = X[:n], X[n:]
for bit in range(1 << n):
    totA = totB = cost = 0
    for i in range(n):
        if bit >> i & 1:
            a, b, c = X[i]
            totA += a
            totB += b
            cost += c

    x[totA][totB] = min(x[totA][totB], cost)

for bit in range(1 << (N-n)):
    totA = totB = cost = 0
    for i in range(N-n):
        if bit >> i & 1:
            a, b, c = Y[i]
            totA += a
            totB += b
            cost += c

    y[totA][totB] = min(y[totA][totB], cost)

ans = INF
M = 405//max(Ma, Mb)
for i, t in enumerate(x):
    for j, s in enumerate(t):
        if s == INF:
            continue
        for k in range(1, M+1):
            I = k*Ma-i
            J = k*Mb-j
            if 0 <= I <= 200 and 0 <= J <= 200:
                ans = min(ans, s + y[I][J])

print(ans if ans < INF else -1)
