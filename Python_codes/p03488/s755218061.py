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
    s=list(input())+['T']
    x,y=map(int,input().split())
    x+=16000
    y+=16000
    ud=[]
    lr=[]
    f=0
    f2=0
    c=0
    for t in s:
        if t=='F':
            if not f:
                x-=1
            else:
                c+=1
        else:
            f=1
            if c:
                if f2:
                    ud.append(c)
                else:
                    lr.append(c)
            c=0
            f2=not f2
    for l,z in [(ud,y),(lr,x)]:
        N=len(l)
        dp=[0]*(N+1)
        dp[0]=1<<16000
        for i in range(N):
            dp[i+1]|=dp[i]<<l[i]|dp[i]>>l[i]
        if not (dp[-1]>>z)&1:
            print('No')
            break
    else:
        print('Yes')
        
    

if __name__ == '__main__':
    main()
