#from numpy import*
#from scipy import*
from collections import* #defaultdict Counter deque appendleft
from fractions import gcd
from functools import* #reduce
from itertools import* #permutations("AB",repeat=2) combinations("AB",2) product("AB",2) groupby
from operator import mul
from bisect import* #bisect_left bisect_right
from heapq import* #heapify heappop heappushpop
from math import factorial
from copy import deepcopy
import sys
#input=sys.stdin.readline  #危険！基本オフにしろ！
sys.setrecursionlimit(10**6)


def main():
    n,*a=map(int,open(0).read().split())
    if abs(max(a))>abs(min(a)):
        b=a.index(max(a))
        print(2*n-1)
        for i in range(n):
            print(b+1,i+1)
        for i in range(n-1):
            print(i+1,i+2)
    else:
        b=a.index(min(a))
        print(2*n-1)
        for i in range(n):
            print(b+1,i+1)
        for i in reversed(range(n-1)):
            print(i+2,i+1)

if __name__ == '__main__':
    main()