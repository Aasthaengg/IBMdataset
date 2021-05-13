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
    A=[0]+list(map(int,input().split()))+[0]
    S=0
    for i in range(N+1):
        S+=abs(A[i+1]-A[i])
    for i in range(N):
        print(S-abs(A[i+1]-A[i])-abs(A[i+2]-A[i+1])+abs(A[i+2]-A[i]))

if __name__ == '__main__':
    main()
