INF = float("inf")

N, M, *ABC = map(int, open(0).read().split())

D = [INF, 0] + [INF] * (N - 1)
E = tuple(zip(*[iter(ABC)] * 3))

for a, b, c in E:
    D[b] = min(D[b], D[a] - c)

ans = D[-1]

for a, b, c in E:
    D[b] = min(D[b], D[a] - c)

print("inf" if ans != D[-1] else -ans)
