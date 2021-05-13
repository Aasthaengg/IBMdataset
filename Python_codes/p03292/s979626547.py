# coding: utf-8

# https://atcoder.jp/contests/abc103
# 11:25-


def main():
    A = list(map(int, input().split()))
    tasks = [[0, 1, 2], [0, 2, 1], [1, 2, 0], [1, 0, 2], [2, 0, 1], [2, 1, 0]]

    ans = 10000000
    for task in tasks:
        cand = abs(A[task[1]]-A[task[0]]) + abs(A[task[2]]-A[task[1]])
        if cand < ans:
            ans = cand
    
    return ans


print(main())
