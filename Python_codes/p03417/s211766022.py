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
    N,M=map(int,input().split())
    if N==M==1:
        ans=1
    elif N==1 or M==1:
        ans=N*M-2
    else:
        ans=(N-2)*(M-2)
    print(ans)

if __name__ == '__main__':
    main()
