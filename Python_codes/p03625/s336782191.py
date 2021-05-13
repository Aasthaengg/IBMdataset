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
    d=defaultdict(int)
    t=[0]
    f=[0]
    for x in A:
        d[x]+=1
        if d[x]==2:
            t.append(x)
        elif d[x]==4:
            f.append(x)
    t.sort()
    f.sort()
    if len(t)>=2:
        print(max(f[-1]**2,t[-1]*t[-2]))
    else:
        print(0)

if __name__ == '__main__':
    main()
