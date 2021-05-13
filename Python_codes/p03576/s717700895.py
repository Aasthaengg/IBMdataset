# -*- coding: utf-8 -*-
import sys
from itertools import combinations,product
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,K=map(int,input().split())
    x,y=[0]*N,[0]*N
    for i in range(N):
        x[i],y[i]=map(int,input().split())
    unique_x,unique_y=list(sorted(list(set(x)))),list(sorted(list(set(y))))
    d_x={z:i for i,z in enumerate(unique_x)}
    d_y={z:i for i,z in enumerate(unique_y)}
    xx=[d_x[z] for z in x]
    yy=[d_y[z] for z in y]
    c=[[0]*N for _ in range(N)]
    for i,j in zip(yy,xx):
        c[i][j]+=1
    s=[[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            s[i+1][j+1]+=s[i][j+1]+s[i+1][j]-s[i][j]+c[i][j]
    xx.sort()
    yy.sort()
    ans=INF*10
    for (x0,x1),(y0,y1) in product(combinations(xx,2),combinations(yy,2)):
        if s[y1+1][x1+1]-s[y1+1][x0]-s[y0][x1+1]+s[y0][x0]>=K:
            ans=min(ans,(unique_y[y1]-unique_y[y0])*(unique_x[x1]-unique_x[x0]))
    print(ans)

if __name__ == '__main__':
    main()
