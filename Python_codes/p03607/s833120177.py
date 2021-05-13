from collections import defaultdict
n = int(input())
dd = defaultdict(int)
for i in range(n):
  s = int(input())
  dd[s]+=1
res = 0
for i in dd.keys():
  if dd[i]%2:
    res+=1
print(res)