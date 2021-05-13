import sys,math,collections

def solve():
    n = int(input())
    L = list(map(int,input().split()))
    L.sort()
    print(L[0],L[-1],sum(L))
    
solve()
