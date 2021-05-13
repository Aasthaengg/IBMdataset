import sys


sys.setrecursionlimit(300000)

to = [[] for _ in range(200005)]
ans: list


def dfs(v, p=-1):
    global ans
    for u in to[v]:
        if u == p: continue
        ans[u] += ans[v]
        dfs(u, v)
    return


def main():
    N, Q = map(int, input().split())
    for _ in range(N-1):
        a, b = map(int, input().split())
        to[a-1].append(b-1)
        to[b-1].append(a-1)
    global ans
    ans = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        ans[p-1] += x
    dfs(0)
    print(*ans)


if __name__ == "__main__":
    main()
