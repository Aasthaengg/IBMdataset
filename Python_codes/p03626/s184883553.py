# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N=int(input())
    S=[list(input()) for _ in range(2)]
    ans=1
    prev=0
    i=0
    while i<N:
        if S[0][i]==S[1][i]:
            ans*=3-prev
            prev=1
            i+=1
        else:
            if prev==0:
                ans*=6
            elif prev==1:
                ans*=2
            else:
                ans*=3
            prev=2
            i+=2
        ans%=MOD
    print(ans)

if __name__ == '__main__':
    main()
