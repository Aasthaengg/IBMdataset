import sys
def input():
    return sys.stdin.readline()[:-1]
N,M=map(int,input().split())
s=[tuple(map(int, input().split())) for i in range(N)]
def me(x,y,z):
    l=[None]*(M+1)
    l[0]=0
    for i,tu in enumerate(s):
        for j in range(M-1,-1,-1):
            if l[j]==None:
                continue
            t=l[j]+tu[0]*x+tu[1]*y+tu[2]*z
            if l[j+1]==None or t>l[j+1]:
                l[j+1]=t
    return l[-1]
print(max(me(1,1,1),me(1,1,-1),me(1,-1,1),me(-1,1,1),me(1,-1,-1),me(-1,-1,1),me(-1,1,-1),me(-1,-1,-1)))
