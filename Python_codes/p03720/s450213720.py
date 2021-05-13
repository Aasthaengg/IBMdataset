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
    N,M=map(int,input().split())
    edge=[[] for _ in range(N)]
    for i in range(M):
        a,b=map(int1,input().split())
        edge[a].append(b)
        edge[b].append(a)
    for i in range(N):
        print(len(edge[i]))

if __name__ == '__main__':
    main()
