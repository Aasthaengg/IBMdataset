#!/usr/bin/env python3
from collections import deque


def Topological_sorting(E):
    N = len(E)
    in_deg = [0]*N
    for i in range(N):        # ２重ループでO(E)
        for to_ in E[i]:
            in_deg[to_] += 1

    ans = [v for v in range(N) if in_deg[v] == 0]
    deq = deque(ans)

    while deq:                  # O(V+E)
        v = deq.popleft()
        for t in E[v]:
            in_deg[t] -= 1
            if in_deg[t] == 0:
                ans.append(t)
                deq.append(t)
    if len(ans) != N:
        return False
    return ans


def main():
    N = int(input())
    A = [None]*N
    for i in range(N):
        A[i] = list(map(lambda x: int(x)-1, input().split()))

    # 0<=i<j<Nを満たすi,jの組を整数へ対応付ける
    MP = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            MP[i][j] = cnt
            MP[j][i] = cnt
            cnt += 1

    out = [[] for _ in range(N*(N-1)//2)]
    # 対戦カードをノードとみなし、閉路検出と最長パス探索を行う
    for i in range(N):
        for j in range(N-2):
            out[MP[i][A[i][j]]].append(MP[i][A[i][j+1]])

    # 閉路検出
    M = N*(N-1)//2

    order = Topological_sorting(out)
    if order is False:
        print(-1)
        return

    # 最長パスを得る
    # 枝の格納方法から、パスは自分の下位の情報から作る。
    # post_order-likeに見る
    depth = [1]*M
    longest = 1
    for i in reversed(order):
        for u in out[i]:
            depth[i] = max(depth[i], 1+depth[u])
        longest = max(depth[i], longest)
    print(longest)
    return


if __name__ == '__main__':
    main()
