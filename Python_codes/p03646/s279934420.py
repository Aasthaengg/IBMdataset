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
    K=int(input())
    q,r=divmod(K,50)
    a=[50+q]*r+[49-r+q]*(50-r)
    print(50)
    print(*a)

if __name__ == '__main__':
    main()
