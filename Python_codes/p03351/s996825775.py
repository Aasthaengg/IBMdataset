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
    a,b,c,d=map(int,input().split())
    YesNo(abs(a-c)<=d or (abs(a-b)<=d and abs(b-c)<=d))

if __name__ == '__main__':
    main()
