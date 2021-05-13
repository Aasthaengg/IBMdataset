# -*- coding: utf-8 -*-
import sys
from itertools import permutations
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,C=map(int,input().split())
    D=[tuple(map(int,input().split())) for _ in range(C)]
    c=[tuple(map(int1,input().split())) for _ in range(N)]
    l=[[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            l[(i+j)%3][c[i][j]]+=1
    ans=INF
    for t in permutations(range(C),3):
        tmp=0
        for i in range(3):
            for j in range(C):
                tmp+=l[i][j]*D[j][t[i]]
        ans=min(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()
