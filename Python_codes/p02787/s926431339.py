h, n = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
A = [x[1] for x in AB]

DP = [float("inf") for _ in range(h+1)]
DP[0] = 0

for i in range(h):
    for damage, cost in AB:
        next_index = min(i+damage, h)
        DP[next_index] = min(DP[next_index], DP[i]+cost)

print(DP[-1])