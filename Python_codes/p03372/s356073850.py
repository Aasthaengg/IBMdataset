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
    N,C=map(int,input().split())
    x,v=[0]*N,[0]*N
    for i in range(N):
        x[i],v[i]=map(int,input().split())
    ans=0
    S=[0]*(N+1)
    for i in range(N):
        S[i+1]=S[i]+v[i]
    x2=[C-x[N-1-i] for i in range(N)]
    v2=list(reversed(v))
    S2=[0]*(N+1)
    for i in range(N):
        S2[i+1]=S2[i]+v2[i]
    
    MAX=[0]*(N+1)
    for i in range(N):
        MAX[i+1]=max(MAX[i],S[i+1]-x[i])
    MAX2=[0]*(N+1)
    for i in range(N):
        MAX2[i+1]=max(MAX2[i],S2[i+1]-x2[i])
    
    x.append(0)
    x2.append(0)
    for i in range(-1,N):
        ans=max(ans,S2[i+1]-x2[i]*2+MAX[-(i+2)],S[i+1]-x[i]*2+MAX2[-(i+2)])
    print(ans)
        

if __name__ == '__main__':
    main()
