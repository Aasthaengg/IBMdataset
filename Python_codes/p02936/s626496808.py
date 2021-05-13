import sys
sys.setrecursionlimit(10**9)


N, Q = map(int, input().split())
to = [[] for _ in range(N)]
ans = [0] * N

for _ in range(N - 1):
    a, b = map(lambda x:int(x) - 1, input().split())
    to[a].append(b)
    to[b].append(a)


def dfs(v, p=-1):
    global ans
    for nv in to[v]:
        if nv == p:
            continue
        ans[nv] += ans[v]
        dfs(nv, v)


def main():
    global ans
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        ans[p] += x
    dfs(0)
    print(*ans)


if __name__ == "__main__":
    main()