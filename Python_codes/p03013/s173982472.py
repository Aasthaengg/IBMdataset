N, M = map(int, input().split())
DIVZ = 10**9+7

steps = [0]*(N+3)
for i in range(M):
    bb = int(input())
    steps[bb] = -1

steps[0] = 1
for i in range(N):
    if steps[i] > 0:
        if steps[i+1] >= 0:
            steps[i+1] += steps[i]
            steps[i + 1] %= DIVZ
        if steps[i+2] >= 0:
            steps[i+2] += steps[i]
            steps[i+2] %= DIVZ

print(steps[N])

