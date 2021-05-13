from collections import Counter,defaultdict,deque
import sys
import copy
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
    
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])

def main():
    n=inp()
    ok=0
    ng=n
    print(0)
    s=input()
    if s=='Vacant':
        return
    for _ in range(19):
        mid = (ok+ng)//2
        print(mid)
        ss=input()
        if ss=='Vacant':
            return
        elif (ss==s and (mid-ok)%2==1) or (ss!=s and (mid-ok)%2==0):
            ng = mid
        else:
            ok = mid
            s = ss


if __name__ == "__main__":
    main()