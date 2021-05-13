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
    N,M,K=map(int,input().split())
    A=list(range(0,N*M+1,N))
    s=set()
    for i in range(M+1):
        for j in range(N+1):
            if A[i]+(M-i*2)*j==K:
                YesNo(1)
                exit()
    YesNo(0)


if __name__ == '__main__':
    main()
