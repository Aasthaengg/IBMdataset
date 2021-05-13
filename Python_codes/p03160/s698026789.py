import sys
sys.setrecursionlimit(1000000)
def solve(n,l,pos):
    if(pos==n):
        return 0
    if(pos==n-1):
        return abs(l[-1]-l[-2])
    if(t[pos]!=-1):
        return t[pos]
    t[pos]=min(abs(l[pos-1]-l[pos])+solve(n,l,pos+1),abs(l[pos-1]-l[pos+1])+solve(n,l,pos+2))
    return t[pos]
n=int(input())
l=list(map(int,input().split()))
global t
t=[-1]*(n+1)
print(solve(n,l,1))