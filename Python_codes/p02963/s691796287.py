import cmath
import sys

INF=10**18
MOD=998244353
MAX=10**5+7

def main():
    S=int(input())

    l=1
    r=10**9

    while l+1<r:
        mid=(l+r)//2
        if mid*mid<=S:
            l=mid
        else:
            r=mid

    ans=[0, 0, r, 1, r*r-S, r]
    print(*ans)

if __name__=='__main__':
    main()
