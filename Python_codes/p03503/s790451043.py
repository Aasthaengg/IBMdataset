# coding: utf-8

# https://atcoder.jp/contests/abc080/tasks/abc080_c
# 15:36-16:15 done

from copy import deepcopy


def main():
    N = int(input())
    F = [None] * N
    for i in range(N):
        F[i] = list(map(int, input().split()))
    P = [None] * N
    for i in range(N):
        P[i] = list(map(int, input().split()))

    # max_benefit = -(10**10)
    n_overlaps_list = []

    def rec(time_i, counts, flag):
        # print(counts)
        # exit()
        # 終章条件
        if time_i == 10:
            if not flag:
                # print(counts)
                n_overlaps_list.append(counts)
            return None

        counts_1 = deepcopy(counts)
        counts_2 = deepcopy(counts)

        for i in range(len(counts)):
            if F[i][time_i] == 1:
                counts_2[i] += 1

        rec(time_i+1, counts_1, flag and True)  # 開かない
        rec(time_i+1, counts_2, False)  # 開く

    rec(0, [0] * N, True)
    # print(n_overlaps_list)

    ans = -(10**10)
    tmp = None
    for n_overlaps in n_overlaps_list:
        candidate = 0
        for i in range(N):
            candidate += P[i][n_overlaps[i]]
        if candidate > ans:
            ans = candidate
            tmp = n_overlaps
    # print(tmp)
    
    return ans


print(main())
