import sys
def input(): return sys.stdin.readline().rstrip()
from functools import reduce
def mod_comb4(n,r,mod=10**9+7):
    if r==1:return n
    elif r==0:return 1
    else:
        num=reduce(lambda x,y:x*y%mod,range(n,n-r,-1))
        den=reduce(lambda x,y:x*y%mod,range(1,r+1))
        return num*pow(den,mod-2,mod)%mod
def main():
    n,k=map(int,input().split())
    mod=10**9+7
    for i in range(1,k+1):
        print(mod_comb4(n-k+1,i)*mod_comb4(k-1,i-1)%mod)

if __name__=='__main__':
    main()