from collections import defaultdict
n,m = map(int, input().split())
d = defaultdict(int)

for i in range(m):
  a,b = map(int, input().split())
  d[a]+=1
  d[b]+=1

for i in d:
  if d[i]%2 ==1:
    print ('NO')
    exit()
print('YES')