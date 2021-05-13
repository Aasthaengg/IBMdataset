import sys
def input():
    return sys.stdin.readline()[:-1]
N=int(input())
s=[[]for i in range(N)]
for i in range(N-1):
    a,b=map(lambda x: int(x)-1,input().split())
    s[a].append(b)
    s[b].append(a)
sys.setrecursionlimit(200000)
lf,ls=[None]*N,[None]*N
lf[0]=0
ls[-1]=0
def hu(n,c,l):
    for i in s[n]:
        if l[i]==None:
            l[i]=c
            hu(i,c+1,l)
hu(0,1,lf)
hu(-1,1,ls)
af=0
for i in range(N):
    if lf[i]<=ls[i]:
        af+=1
if af*2>N:
    print("Fennec")
else:
    print("Snuke")