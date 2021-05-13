from itertools import permutations


def main():
    towns, roads, visit = map(int, input().split())
    visit_order = [int(x) - 1 for x in input().split()]
    dist = [[float("inf") for _ in range(towns)] for _ in range(towns)]
    for _ in range(roads):
        a, b, d = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = d
        dist[b][a] = d
    for k in range(towns):
        for i in range(towns):
            for j in range(towns):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    answer = float("inf")
    for p in permutations(visit_order):
        now = 0
        for i in range(visit - 1):
            now += dist[p[i]][p[i + 1]]
        answer = min(answer, now)
    print(answer)


if __name__ == '__main__':
    main()

