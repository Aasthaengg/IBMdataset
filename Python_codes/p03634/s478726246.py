import sys
sys.setrecursionlimit(10**9)


N = int(input())
to = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    a, b, = a - 1, b - 1
    to[a].append((c, b))
    to[b].append((c, a))

Q, K = map(int, input().split())
K -= 1
query = [list(map(lambda x:int(x) - 1, input().split())) for _ in range(Q)]
depth = [0] * N

def dfs(v, d, p=-1):
    depth[v] = d
    for cost, nv in to[v]:
        if nv == p:
            continue
        dfs(nv, d + cost, v)


def main():
    dfs(K, 0)
    for x, y in query:
        print(depth[x] + depth[y])


if __name__ == "__main__":
    main()