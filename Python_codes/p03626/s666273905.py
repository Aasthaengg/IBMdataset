#from numpy import*
#from scipy import*
from collections import* #defaultdict Counter deque appendleft
from fractions import gcd
from functools import* #reduce
from itertools import* #permutations("AB",repeat=2) combinations("AB",2) product("AB",2) groupby accumulate
from operator import mul
from bisect import* #bisect_left bisect_right
from heapq import* #heapify heappop heappushpop
from math import factorial,pi
from copy import deepcopy
import sys
#input=sys.stdin.readline  #危険！基本オフにしろ！
sys.setrecursionlimit(10**6)



def main():
    input()
    x=[len(list(v))for k,v in groupby(input())]
    if x[0]==1:
        ans=3
    else:
        ans=6
    mod=10**9+7
    for i in range(1,len(x)):
        if x[i-1]==1 and x[i]==1:
            ans*=2%mod
        elif x[i-1]==1 and x[i]==2:
            ans*=2%mod
        elif x[i-1]==2 and x[i]==2:
            ans*=3%mod
    print(ans%mod)
if __name__ == '__main__':
    main()
