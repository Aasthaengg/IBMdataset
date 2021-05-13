import sys
def input():
    return sys.stdin.readline()[:-1]
N,C=map(int,input().split())
l=[[0]*10**5 for i in range(C)]
for i in range(N):
    s,t,c=map(lambda x: int(x)-1,input().split())
    for j in range(s,t+1):
        l[c][j]=1
a=0
for i in range(10**5):
    t=0
    for j in range(C):
        if l[j][i]:
            t+=1
    if t>a:
        a=t
print(a)