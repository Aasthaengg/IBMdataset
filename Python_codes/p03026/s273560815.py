from collections import defaultdict
import sys


sys.setrecursionlimit(10**6)


def main():
    N = int(input())
    adj = defaultdict(list)
    for _ in range(N - 1):
        a, b = list(map(int, input().split()))
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    C = list(map(int, input().split()))

    # 深さ優先で番号の大きい順に埋めていく
    C.sort(reverse=True)
    ans = [0] * N

    def dfs(node=0, parent=None, c_index=0):
        ans[node] = C[c_index]
        next_c_index = c_index + 1
        for child in adj[node]:
            if child == parent:
                continue
            next_c_index = dfs(child, node, next_c_index)
        return next_c_index

    dfs()
    print(sum(C[1:]))
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
