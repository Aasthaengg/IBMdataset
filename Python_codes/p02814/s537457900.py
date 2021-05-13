import unittest
from io import StringIO
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    n, m = map(int, input().split())
    if n==1:
        a=int(input())
        print(-(-(m//(a//2)) // 2))

    else:
        A = list(map(int, input().split()))
        B = [0]*n
        for i in range(n):
            B[i] = A[i]//2

        for i in range(n):
            cnt = 0
            val = B[i]
            while val % 2 == 0:
                val //= 2
                cnt += 1
            if i == 0:
                temp = cnt
            else:
                if cnt != temp:
                    ok = False
                    break
                if i == n-1:
                    ok = True

        if ok:
            from functools import reduce
            from fractions import gcd

            def lcm(A, B):
                return A * B // gcd(A, B)

            # リストを引数にとる
            l = reduce(lcm, B)
            print(-(-(m//l) // 2))

        else:
            print(0)


resolve()
