# -*- coding: utf-8 -*-
import sys
from collections import Counter
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N=int(input())
    A=list(map(int,input().split()))
    c=Counter(A)
    if N%2:
        if not (0 in c and c[0]==1):
            print(0)
            exit()
        for k in range(2,N,2):
            if not (k in c and c[k]==2):
                print(0)
                exit()
    else:
        for k in range(1,N,2):
            if not (k in c and c[k]==2):
                print(0)
                exit()
    print(pow(2,N//2,MOD))

if __name__ == '__main__':
    main()
