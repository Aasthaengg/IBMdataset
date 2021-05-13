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
    edge=[]
    for i in range(M):
        a,b,c=map(int1,input().split())
        c+=1
        edge.append((a,b,-c))
    d=[INF]*N
    d[0]=0
    f=False
    for i in range(N*2):
        for a,b,c in edge:
            if d[b]>d[a]+c:
                if i<N-1:
                    d[b]=d[a]+c
                else:
                    if d[a]<10**17:
                        d[b]=-INF
                    if b==N-1:
                        f=True
    if f:
        print('inf')
    else:
        print(-d[N-1])

if __name__ == '__main__':
    main()
