import sys
def input():
    return sys.stdin.readline()[:-1]
sys.setrecursionlimit(200000)
H,W=map(int,input().split())
S=[input() for i in range(H)]
l=[[0]*(W+2) for i in range(H+2)]
for i in range(1,H+1):
    for j in range(1,W+1):
        l[i][j]=1
a,c=0,1
def nu(h,w):
    global c,b
    if S[h-1][w-1]=="#":
        b+=1
    if l[h-1][w] and S[h-1][w-1]!=S[h-2][w-1]:
        l[h-1][w]=0
        c+=1
        nu(h-1,w)
    if l[h+1][w] and S[h-1][w-1]!=S[h][w-1]:
        l[h+1][w]=0
        c+=1
        nu(h+1,w)
    if l[h][w-1] and S[h-1][w-1]!=S[h-1][w-2]:
        l[h][w-1]=0
        c+=1
        nu(h,w-1)
    if l[h][w+1] and S[h-1][w-1]!=S[h-1][w]:
        l[h][w+1]=0
        c+=1
        nu(h,w+1)
for i in range(1,H+1):
    for j in range(1,W+2):
        if not l[i][j]:
            continue
        b,c=0,1
        l[i][j]=0
        nu(i,j)
        a+=b*(c-b)
print(a)

