from collections import defaultdict
n=int(input())
s=["".join(sorted(input())) for _ in range(n)]

d = defaultdict(int)
for a in s:
  d[a]+=1
c=0
for a in d.values():
  if a>1:
    c+=a*(a-1)//2
print(c)