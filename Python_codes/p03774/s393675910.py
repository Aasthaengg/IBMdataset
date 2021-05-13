import sys

N,M=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(N)]
c=[list(map(int,input().split())) for _ in range(M)]
inf=10**9
def findcp(st):
    dist=inf
    i=0
    for j in range(M):
        if abs(st[0]-c[j][0])+abs(st[1]-c[j][1])<dist:
            dist=abs(st[0]-c[j][0])+abs(st[1]-c[j][1])
            i=j
    return i+1

for i in range(N):
    print(findcp(s[i]))


