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
    p=list(map(int,input().split()))
    c=0
    f=False
    for i in range(N):
        if p[i]==i+1:
            if f:
                f=False
            else:
                c+=1
                f=True
        else:
            f=False
    print(c)

if __name__ == '__main__':
    main()
