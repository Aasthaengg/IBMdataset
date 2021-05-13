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
    M,K=map(int,input().split())
    if K>2**M-1:
        print(-1)
    elif M==1:
        if K==0:
            print(0,0,1,1)
        else:
            print(-1)
    else:
        ans=[i for i in range(2**M) if i!=K]+[K]+[i for i in range(2**M-1,-1,-1) if i!=K]+[K]
        print(*ans)

if __name__ == '__main__':
    main()
