from sys import stdin, setrecursionlimit
from collections import Counter, deque, defaultdict
from math import floor, ceil
from bisect import bisect_left
from itertools import combinations
setrecursionlimit(100000)

INF = int(1e10)
MOD = int(1e9 + 7)

def main():
    from builtins import int, map
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    

    count_even, count_odd = 0, 0
    for a in A:
        if a % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    
    ans = -1
    # print(N, P, A)
    # print(count_even, count_odd)
    if count_odd == 0:
        # 偶数しかない
        if P == 0:
            # 偶数にしたい => どれでもOK
            ans = 2 ** N
        else:
            # 奇数枚は食べられない
            ans = 0
    else:
        # 奇数が1以上存在するので，ある1つ以外の和Sを考える
        # S is odd: 食べたらeven，食べないとodd => 2 ^ (N-1) パターン
        # S is even: 食べたらodd，食べないとeven
        ans = 2 ** (N - 1)
    print(ans)


if __name__ == '__main__':
    main()
