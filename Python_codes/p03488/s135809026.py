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
    *s,=map(len,input().split("T"))
    x,y=map(int,input().split())
    start=s[0]
    n=s[2::2]
    m=s[1::2]
#    print(n,m)
    dx={start}
    dy={0}
#    print(dx)
    for i in n:
        dx={r+j for j in dx for r in{-i,i}}
#        print(dx)
    for i in m:
        dy={r+j for j in dy for r in{-i,i}}
#        print(dy)
    if x in dx and y in dy:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()