#

import sys
input=sys.stdin.readline

MOD=10**9+7
            
def main():
    N=int(input())
    A=list(map(int,input().split()))
    if N==1:
        print(1)
        exit()
    kl=[0]*(10**6+1)
    for j in range(N):
        n=A[j]
        for i in range(2,int((n)**0.5)+1):
            if n%i==0:
                cnt=0
                while(n%i==0):
                    n//=i
                    cnt+=1
                if kl[i]<cnt:
                    kl[i]=cnt
        if n!=1:
            if kl[int(n)]<1:
                kl[int(n)]=1
                
    lcm=1
    for i in range(2,10**6+1):
        lcm*=i**kl[i]
        lcm%=MOD
    ans=0
    for i in range(N):
        ans+=lcm*pow(A[i],MOD-2,MOD)
        ans%=MOD
    print(ans)
    
    
    
if __name__=="__main__":
    main()
