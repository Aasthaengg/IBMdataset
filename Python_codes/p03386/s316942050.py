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
    A,B,K=map(int,input().split())
    l=[i for i in range(A,min(A+K,B+1))]+[i for i in range(B,max(B-K,A-1),-1)]
    l=list(set(l))
    l.sort()
    for a in l:
        print(a)

if __name__ == '__main__':
    main()
