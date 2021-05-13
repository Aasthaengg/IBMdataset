import sys
def input():
    return sys.stdin.readline()[:-1]
N,C=map(int,input().split())
D=[tuple(map(int, input().split())) for i in range(C)]
c=[tuple(map(lambda x:int(x)-1, input().split())) for i in range(N)]
iw=[[0]*C for i in range(3)]
l=[[] for i in range(3)]
for i in range(N):
    for j in range(N):
        l[(i+j)%3].append(c[i][j])
for i in range(3):
    for j in range(C):
        for k in l[i]:
            iw[i][j]+=D[k][j]
a=10**9
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i!=j and i!=k and j!=k:
                a=min(a,iw[0][i]+iw[1][j]+iw[2][k])
print(a)