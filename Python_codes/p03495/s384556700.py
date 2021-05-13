# -*- coding: utf-8 -*-
import sys
from collections import Counter
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    c=Counter(A)
    m=c.most_common()[::-1]
    ans=0
    for _,n in m[:-K]:
        ans+=n
    print(ans)
    

if __name__ == '__main__':
    main()
