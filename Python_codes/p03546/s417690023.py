import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter
    import networkx as nx
    h, w = map(int, readline().split())
    G = nx.DiGraph()

    for i in range(10):
        costs = list(map(int, readline().split()))
        for j, cost in enumerate(costs):
            if i != j:
                G.add_edge(i, j, weight=cost)

    d = nx.algorithms.floyd_warshall(G)

    counter = Counter()
    for _ in range(h):
        nums = list(map(int, readline().split()))
        counter.update(nums)
    ans = 0
    for num in range(10):
        ans += counter[num] * d[num][1]

    print(ans)


if __name__ == '__main__':
    main()
