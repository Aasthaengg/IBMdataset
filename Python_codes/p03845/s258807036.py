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
    T=list(map(int,input().split()))
    S=sum(T)
    M=int(input())
    for _ in range(M):
        p,x=map(int,input().split())
        p-=1
        print(S-T[p]+x)

if __name__ == '__main__':
    main()
