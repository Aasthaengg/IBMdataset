from sys import stdin
import numpy as np
from numba import njit
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    s=readline().strip()
    ans=s.count("R")*s.count("G")*s.count("B")
    s=np.array([0 if s[i]=="R" else 1 if s[i]=="G" else 2 for i in range(n)],dtype=np.int64)

    print(f(n,ans,s))

@njit("i8(i8,i8,i8[:])")
def f(n,ans,s):
    for i in range(n):
        for j in range(i+1,n):
            k=2*j-i
            if k>=n: break
            if s[i]!=s[j] and s[j]!=s[k] and s[k]!=s[i]:
                ans-=1
    return ans

if __name__=="__main__":
    main()