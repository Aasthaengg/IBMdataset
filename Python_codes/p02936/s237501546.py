import sys

sys.setrecursionlimit(10**7)


def dfs(s, to, ans, p=-1):
    for v in to[s]:
        if v == p: continue
        ans[v] += ans[s]
        dfs(v, to, ans, s)


def main():
    N, Q = map(int, input().split())
    to = [[] for _ in range(N)]
    ans = [0] * N

    for _ in range(N - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        to[a].append(b)
        to[b].append(a)
    
    for _ in range(Q):
        p, x = map(int, input().split())
        ans[p-1] += x
    dfs(0, to, ans)
    
    print(*ans)


if __name__ == "__main__":
    main()
