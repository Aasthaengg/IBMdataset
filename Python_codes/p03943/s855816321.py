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
    l=list(map(int,input().split()))
    for i in range(3):
        if sum(l)-l[i]==l[i]:
            print('Yes')
            exit()
    print('No')
    

if __name__ == '__main__':
    main()
