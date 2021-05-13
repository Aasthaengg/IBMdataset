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
    l=[]
    for i in range(N):
        l.append(list(map(int,input().split())))
    l.sort(key=lambda t:(t[2],t[1]))
    a=[0]*(10**5+1)
    ss,tt,cc=-1,-1,-1
    for s,t,c in l:
        if s==tt and c==cc:
            a[tt]+=1
            a[t]-=1
        else:
            a[s-1]+=1
            a[t]-=1
        ss,tt,cc=s,t,c
    ans=0
    tmp=0
    for x in a:
        tmp+=x
        ans=max(ans,tmp)
    print(ans)
            

if __name__ == '__main__':
    main()
