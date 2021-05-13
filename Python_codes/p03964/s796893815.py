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
    T,A=map(int,input().split())
    for _ in range(N-1):
        t,a=map(int,input().split())
        res=max(-(-T//t),-(-A//a))
        T,A=t*res,a*res
    print(T+A)

if __name__ == '__main__':
    main()
