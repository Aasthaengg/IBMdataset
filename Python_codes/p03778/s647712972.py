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
    W,a,b=map(int,input().split())
    if a<=b<=a+W or a<=b+W<=a+W or b<=a<=b+W or b<=a+W<=b+W:
        print(0)
    else:
        if a<b:
            print(b-(a+W))
        else:
            print(a-(b+W))

if __name__ == '__main__':
    main()
