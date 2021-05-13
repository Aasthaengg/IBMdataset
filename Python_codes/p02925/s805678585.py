#!/usr/bin/env python3
import sys
from collections import deque
import heapq
INF = float("inf")


def main():
    # 10**6くらいのループ
    # 毎回、logN以内で閉路を検出できると嬉しい
    # 見るべき場所は、新しく追加したところだけで、即座にわかるのでO(1)か
    N = int(input())
    A = [None]*N
    for i in range(N):
        A[i] = list(map(lambda x: int(x)-1, input().split()))
    # print(A)

    # それぞれの選手の手合進行
    indices = [0]*N
    E = [-1 for _ in range(N)]
    change = []
    for i in range(N):
        # 選手iは次選手A[i][indices[i]]と勝負したい
        E[i] = A[i][indices[i]]
        if E[E[i]] == i:
            # 勝負成立
            change.append(i)
            change.append(E[i])
            indices[i] += 1
            indices[E[i]] += 1
    if len(change) == 0:
        # print("一巡目終了")
        print(-1)
        return

    ans = 0
    while len(change) > 0:
        # print("change", change)
        # print("indices", indices)
        new_change = []
        ans += 1
        for c in change:
            # print("変更", c)
            if indices[c] == N-1:
                continue
            E[c] = A[c][indices[c]]
            if E[E[c]] == c:
                # 勝負成立
                # print("勝負成立, ", c, " vs ", E[c])
                # print(indices)
                new_change.append(c)
                new_change.append(E[c])
                indices[c] += 1
                indices[E[c]] += 1
        change = new_change

    flag = True
    for i in range(N):
        if indices[i] != N-1:
            flag = False
            break
    if flag is False:
        # print(indices)
        print(-1)
        return
    print(ans)

    return


if __name__ == '__main__':
    main()
