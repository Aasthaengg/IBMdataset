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
    a=list(map(int,input().split()))
    t=0
    f=0
    for i in range(N):
        if a[i]%4==0:
            f+=1
        elif a[i]%2==0:
            t+=1
    YesNo(N//2<=f+t//2)

if __name__ == '__main__':
    main()
