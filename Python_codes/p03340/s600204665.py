# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
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
    ans=0
    left=0
    S,X=0,0
    for right in range(N):
        S+=A[right]
        X^=A[right]
        if S==X:
            continue
        else:
            ans+=(right-left)*(right-left+1)//2
            for left in range(left,right):
                S-=A[left]
                X^=A[left]
                if S==X:
                    left+=1
                    break
            ans-=(right-left)*(right-left+1)//2
    right+=1
    ans+=(right-left)*(right-left+1)//2
    print(ans)

if __name__ == '__main__':
    main()
