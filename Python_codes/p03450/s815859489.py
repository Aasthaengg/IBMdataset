import sys
def input():
    return sys.stdin.readline()[:-1]
N,M=map(int,input().split())
s=[[]for i in range(N)]
for i in range(M):
    L,R,D=map(int,input().split())
    s[L-1].append((R-1,D))
    s[R-1].append((L-1,-D))
sys.setrecursionlimit(200000)
l=[None]*N
a=1
def hu(n,x):
    global a
    for i in s[n]:
        if l[i[0]]==None:
            l[i[0]]=x+i[1]
            hu(i[0],x+i[1])
        else:
            if x+i[1]!=l[i[0]]:
                a=0
for i in range(N):
    if l[i]==None:
        l[i]=0
        hu(i,0)
print("Yes" if a else "No")