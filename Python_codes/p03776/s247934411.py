import sys
input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import heapq
import bisect
import copy
import math
from collections import defaultdict, Counter

def warshall_floyd(d, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i * N +j] = min(d[i * N +j], d[i * N + k] + d[k * N + j])
    return d
MOD = 10**9 + 7
INF = 10**10

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    n,a,b = getlist()
    nums = getlist()

    cnt = Counter(nums)

    cnt = sorted(cnt.items(), key=lambda x: -x[0])
    # print(cnt)
    ans = 0
    tmp_max = 0
    res = 0
    for i in range(a, b+1):
        remain = i
        acc_val = 0
        for it in cnt:
            if it[1] <= remain:
                remain -= it[1]
                acc_val += it[1] * it[0]

            else:
                acc_val += remain * it[0]
                cmb = comb(it[1], remain)
                mean = acc_val / i
                res += comb(50, i)
                if mean == tmp_max:
                    ans += cmb
                elif mean > tmp_max:
                    tmp_max = mean
                    ans = cmb
                # print(mean, acc_val, ans, res)
                break

            if remain == 0:
                mean = acc_val / i
                if mean == tmp_max:
                    ans  += 1
                elif mean > tmp_max:
                    tmp_max = mean
                    ans = 1

                break
    print(tmp_max)
    print(ans)

    # res = 0
    # for i in range(1, 51):
    #     res += comb(50, i)
    #
    # print(res)


if __name__ == '__main__':
    main()

"""
9999
3

2916
"""