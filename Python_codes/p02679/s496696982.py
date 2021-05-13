import sys
input=sys.stdin.readline
from collections import defaultdict
from math import gcd

def main():
    mod=1000000007
    n=int(input())
    AB=[tuple(map(int,input().split())) for _ in range(n)]
    Cnt=defaultdict(int)
    zero=0
    for a,b in AB:
        if a==0 and b==0:
            zero+=1
        elif a==0:
            Cnt[(0,1)]+=1
        elif b==0:
            Cnt[(1,0)]+=1
        elif b!=0 and a>0:
            Cnt[(a//gcd(a,b),b//gcd(a,b))]+=1
        else: #b!=0 and a<0:
            Cnt[(-a//gcd(a,b),-b//gcd(a,b))]+=1
    ans=1
    for Key in list(Cnt.keys()):
        if Key!=(0,1) and Key!=(1,0):
            a,b=Key
            if b>0:
                ans*=pow(2,Cnt[Key],mod)+pow(2,Cnt[(b,-a)],mod)-1
                ans%=mod
                Cnt[(b,-a)]=0
            else:
                ans*=pow(2,Cnt[Key],mod)+pow(2,Cnt[(-b,a)],mod)-1
                ans%=mod
                Cnt[(-b,a)]=0
            Cnt[Key]=0
        else:
            ans*=pow(2,Cnt[(0,1)],mod)+pow(2,Cnt[(1,0)],mod)-1
            ans%=mod
            Cnt[(0,1)],Cnt[(1,0)]=0,0
    print((ans-1+zero)%mod)
    
if __name__=='__main__':
    main()