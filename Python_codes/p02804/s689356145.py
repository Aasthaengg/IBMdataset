#

import sys
input=sys.stdin.readline
MOD=10**9+7

fact=[1]*(10**5+1)
for i in range(1,10**5+1):
    fact[i]=(fact[i-1]*i)%MOD
    
def comb(n,r):
    nhri=pow(fact[n-r],MOD-2,MOD)
    ri=pow(fact[r],MOD-2,MOD)
    return fact[n]*nhri*ri


def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    
    A.sort()
    maxsum=0
    for i in range(K-1,N):
        maxsum+=comb(i,K-1)*A[i]
        maxsum%=MOD
    
    A.sort(reverse=True)
    minsum=0
    for i in range(K-1,N):
        minsum+=comb(i,K-1)*A[i]
        minsum%=MOD
        
    print((maxsum-minsum)%MOD)
    
    
if __name__=="__main__":
    main()
