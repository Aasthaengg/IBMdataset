from sys import stdin
import numpy as np
from numba import njit
def main():
    #入力
    readline=stdin.readline
    n,k=map(int,readline().split())
    a=np.array(list(map(int,readline().split())),dtype=np.int64)

    cnt=0
    while cnt<k:
        s=f(n,a)
        a=np.cumsum(s)
        cnt+=1
        if a[a==n].size==n:
            break

    print(*a)

@njit("i8[:](i8,i8[:])",cache=True)
def f(n,a):
    s=np.zeros(n,dtype=np.int64)
    for i in range(n):
        x_min=i-a[i]
        x_max=i+a[i]+1
        s[max(0,x_min)]+=1
        if n-1<x_max:
            pass
        else:
            s[x_max]-=1
    return s

if __name__=="__main__":
    main()