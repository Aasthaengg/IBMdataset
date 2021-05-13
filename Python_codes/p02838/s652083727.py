from sys import stdin
import numpy as np
def main():
    #入力
    readline=stdin.readline
    mod=10**9+7
    n=int(readline())
    a=list(map(int,readline().split()))
    a=np.array(a,dtype=np.int64)

    b=np.array([((a>>i)&1).sum() for i in range(61)],dtype=np.int64)
    c=np.full(61,n,dtype=np.int64)-b
    d=b*c
    d%=mod

    ans=0
    now=1
    for i in range(60):
        ans+=d[i]*now
        ans%=mod
        now*=2
        now%=mod

    print(ans)

if __name__=="__main__":
    main()