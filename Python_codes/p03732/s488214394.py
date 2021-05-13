from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(int)
d[0]=0
for _ in range(n):
       w,u=map(int,input().split())
       for i,j in d.copy().items():
              if i+w<=m:d[i+w]=max(d[i+w],j+u)
print(max(d.values()))