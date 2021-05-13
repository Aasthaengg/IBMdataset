import collections # deque, Counter
import itertools # accumulate, compress, permutations(nPr), combinations(nCr)
# import bisect
import math # factorical（階乗)
# import heapq
# from fractions import gcd # >=Python3.5 # lcm（最小公倍数） = (a*b)//gcd(a,b)
# from fractions import Fraction
# from math import gcd # <Python3.5

# input = sys.stdin.readline
# def main():

#---------------------------------------------------------

n  = int(input())
li = [list(map(int,input().split())) for i in range(n)]

cnt = math.factorial(n-1)
ans = 0

chkli = itertools.permutations(range(n),2)

for i, v in enumerate(chkli):
    ans += ((abs((li[v[0]][0]) - (li[v[1]][0])) ** 2) + (abs((li[v[0]][1]) - (li[v[1]][1])) ** 2)) **.5 * cnt

print(ans/(math.factorial(n)))