import sys
input = sys.stdin.readline
INF = 10**20
MOD = 10**9 + 7
import numpy as np

def main():
    n,a,b = map(int,input().split())
    H = np.array([int(input()) for _ in range(n)])

    a -= b
    def ok(x): #x回の爆発で倒せるか
        list = (H - b * x + a - 1)//a
        return sum(list[list>0]) <=  x
    
    l = -1
    r = 10 ** 10
    while r - l > 1:
        mid = (r + l)//2
        if ok(mid):
            r = mid
        else:
            l = mid  
    print(r)

if __name__=='__main__':
    main()