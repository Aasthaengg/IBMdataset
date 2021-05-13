# まず, 答えは総和の約数となる
# 恐らく約数ごとに条件が成り立つか調べることになる

# 答えをdと仮定したとき, 各値はdの倍数となる
# 総和をどのように振り分けたらK以下で全てdの倍数になるか調べるのは無理
# そこでmod(d)で考えることにする
# 各値についてdで割った余りを記録していく
# それをソートして両端から-1/+1していけば
# 必ず全て0にでき, その操作回数もO(N)で分かる

# コードは累積和で境界を求めてる

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    from fractions import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    def yakusuu(N):
        n = int(N**.5)+1
        res1 = []
        res2 = []
        for i in range(1, n):
            if N%i==0:
                res1.append(i)
                if N!=i**2:
                    res2.append(N//i)
        res2.reverse()
        return res1+res2
        # 約数のリストを返す

    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    
    kouho = yakusuu(sum(a))

    for i in kouho[::-1]:
        nega = [0]*n
        posi = [0]*n
        for j in range(n):
            posi[j] = a[j] % i
        posi.sort()
        for j in range(n):
            nega[j] = posi[j] - i
        posi = [0] + posi
        nega = [0] + nega
        posi = list(accumulate(posi))
        nega = list(accumulate(nega))
        for j in range(1, n+1):
            if posi[j] == -(nega[-1]-nega[j]):
                total = posi[j]
                break
        if total <= k:
            print(i)
            break
        
if __name__ == '__main__':
    main()