MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from itertools import accumulate

def ok(x,A,Acum):
    size = Acum[x]
    for creature in A[x + 1:]:
        if creature  <= 2*size:
            size += creature
    if size == Acum[-1]:
        return True
    return False

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    Acum = list(accumulate(A))
    
    l = -1
    r = N
    while r - l > 1:
        mid = (r + l)//2
        if ok(mid,A,Acum):
            r = mid
        else:
            l = mid
    print(N - r)  
if __name__ == '__main__':
    main()