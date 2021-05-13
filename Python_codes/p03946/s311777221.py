# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,T=map(int,input().split())
    A=list(map(int,input().split()))
    m=INF
    diff=0
    for i in range(N):
        m=min(m,A[i])
        diff=max(diff,A[i]-m)
    d=defaultdict(int)
    dd=defaultdict(lambda:[0,0])
    for i in range(N):
        res=d[A[i]-diff]
        if res>0:
            dd[A[i]][0]+=1
            dd[A[i]][1]+=res
        d[A[i]]+=1
    ans=0
    for l in dd.values():
        ans+=min(l)
    print(ans)
    

if __name__ == '__main__':
    main()
