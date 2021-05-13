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
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    SUM=sum(A)
    l=[]
    for i in range(1,int(SUM**0.5)+1):
        if SUM%i==0:
            l.append(i)
            l.append(SUM//i)
    ans=0
    for x in l:
        B=[A[i]%x for i in range(N)]
        B.sort()
        S_m=[0]*(N+1)
        S_p=[0]*(N+1)
        for i in range(N):
            S_m[i+1]=S_m[i]+B[i]
            S_p[i+1]=S_p[i]+x-B[i]
        for i in range(N+1):
            if max(S_m[i],S_p[N]-S_p[i])<=K:
                ans=max(ans,x)
                break
    print(ans)

if __name__ == '__main__':
    main()