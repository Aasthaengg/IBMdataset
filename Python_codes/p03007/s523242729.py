import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input()) # n=1
def inpm(): return map(int,input().split()) # x=1,y=2
def inpl(): return list(map(int, input().split())) # a=[1,2,3,4,5,...,n]
def inpls(): return list(input().split())  # a=['1','2','3',...,'n']
def inplm(n): return list(int(input()) for _ in range(n)) # x=[] 複数行
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)] # [[1,1,1,1],[2,2,2,2],[3,3,3,3]] 
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)]) # [[1,1,1,1],[2,2,2,2],[3,3,3,3]] 
def graph():
    n=inp()
    g=[[] for _ in range(n)]
    for i in range(n):
        a = inp()
        a -= 1
        g[i].append(a)
        g[a].append(i)
    return n,g

def main():
    n = inp()
    a = inpl()
    a.sort()
    ans = []
    cnt = 0
    if a[0] >= 0:
        x = a[0]
        for i in range(n-2):
            ans.append((x,a[i+1]))
            x -= a[i+1]
        ans.append((a[n-1],x))
        cnt = a[n-1]-x        
    elif a[n-1] <= 0:
        x = a[n-1]
        for i in range(n-1):
            ans.append((x,a[i]))
            x -= a[i]
        cnt = x
    else:
        for i in range(n):
            if a[i] >= 0:
                x = a[i-1]
                index = i
                break
        for i in range(index+1,n):
            ans.append((x,a[i]))
            x -= a[i]
        a[index-1] = x
        x = a[index]
        for i in range(index):
            ans.append((x,a[i]))
            x -= a[i]
        cnt = x        
    print(cnt)
    for i in range(n-1):
        print(*ans[i])

if __name__ == "__main__":
    main()