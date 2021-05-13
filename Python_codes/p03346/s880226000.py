import sys
from sys import stdin, stdout

rem=10**9+7
sys.setrecursionlimit(10 ** 6)
take = lambda: map(int, stdin.readline().split())

n=input()
ans=[1 for i in range(n+1)]
pos={}
for i in range(1,n+1):
    x=take()[0]
    pos[x]=i
for i in range(n-1,0,-1):
    if pos[i]<pos[i+1]:
        ans[i]=ans[i+1]+1
#print(ans)
print n-max(ans)