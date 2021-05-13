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
    N,x=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    for i in range(N):
        ans+=max(a[i]-x,0)
        a[i]=min(a[i],x)
    for i in range(N-1):
        if a[i]+a[i+1]>x:
            ans+=a[i]+a[i+1]-x
            a[i+1]=x-a[i]
    print(ans)

if __name__ == '__main__':
    main()
