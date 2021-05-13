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
    x=int(input())
    ans=x//11
    x-=ans*11
    ans*=2
    ans+=-(-x//6)
    print(ans)

if __name__ == '__main__':
    main()
