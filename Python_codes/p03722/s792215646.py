def main():
    INF = float("inf")

    N, M, *ABC = map(int, open(0).read().split())

    D = [0] + [INF] * (N - 1)
    E = tuple((a - 1, b - 1, -c) for a, b, c in zip(*[iter(ABC)] * 3))

    for _ in range(N - 1):
        for a, b, c in E:
            if D[a] == INF:
                continue
            D[b] = min(D[b], D[a] + c)

    ans = D[-1]
    neg = [False] * N

    for _ in range(N):
        for a, b, c in E:
            if D[a] == INF:
                continue

            if D[b] > D[a] + c:
                D[b] = D[a] + c
                neg[b] = True

            if neg[a]:
                neg[b] = True

    print("inf" if ans != D[-1] else -ans)

main()
