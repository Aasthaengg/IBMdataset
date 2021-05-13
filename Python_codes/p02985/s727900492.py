def main():
    from collections import deque
    from functools import reduce
    import sys
    input = sys.stdin.readline

    MOD = 10 ** 9 + 7

    def mod_mul(a, b):
        return a * b % MOD

    N, K = map(int, input().split())

    Graph = tuple(set() for _ in range(N))
    for _ in range(N - 1):
        a, b = (int(x) - 1 for x in input().split())
        Graph[a].add(b)
        Graph[b].add(a)

    dq = deque()
    color = [-1] * N
    color[0] = K
    used = 0
    for u in Graph[0]:
        color[u] = K - 1 - used
        used += 1
        dq.append(u)

    while dq:
        v = dq.popleft()
        used = 0
        for u in Graph[v]:
            if ~color[u]:
                continue
            color[u] = K - 2 - used
            used += 1
            dq.append(u)

    ans = reduce(mod_mul, color)

    print(ans)


if __name__ == '__main__':
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())
