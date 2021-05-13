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
    N,A,B=map(int,input().split())
    X=list(map(int,input().split()))
    z=B//A
    ans=0
    for i in range(N-1):
        if X[i+1]-X[i]>z:
            ans+=B
        else:
            ans+=(X[i+1]-X[i])*A
    print(ans)

if __name__ == '__main__':
    main()
