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
    a,b,c=map(int,input().split())
    if a==b:
        print(c)
    elif a==c:
        print(b)
    else:
        print(a)

if __name__ == '__main__':
    main()
