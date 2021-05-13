import sys
input=sys.stdin.readline

n,m=map(int,input().split())

from collections import Counter
l=[]
for _ in range(m):
    l+=list(map(int,input().split()))

c=Counter(l)
print("YES" if all(v%2==0 for v in c.values()) else "NO")
