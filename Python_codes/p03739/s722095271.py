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
    n=int(input())
    a=list(map(int,input().split()))
    ans=INF
    for f in range(2):
        s=0
        tmp=0
        for x in a:
            s+=x
            if f and s<=0:
                tmp+=1-s
                s=1
            elif not f and s>=0:
                tmp+=s+1
                s=-1
            f=not f
        ans=min(ans,tmp)
    print(ans)
    
    

if __name__ == '__main__':
    main()
