import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
n=int(input())
p=[int(input())-1 for _ in range(n)]
a=[0]*n
for i in range(n):
    a[p[i]]=i
l=1
ans=1
for i in range(n-1):
    if a[i]<a[i+1]:
        l+=1
    else:
        ans=max(ans,l)
        l=1
ans=max(ans,l)
print(n-ans)