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
    l=[0]*(N+1)
    for i in range(1,N+1):
        a=2
        while i>1:
            if i%a==0:
                l[a]+=1
                i//=a
            else:
                a+=1
    
    ans=1
    for x in l:
        ans*=x+1
        ans%=MOD
    print(ans)

if __name__ == '__main__':
    main()
