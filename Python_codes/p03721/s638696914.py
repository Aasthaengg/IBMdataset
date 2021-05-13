import collections
[n,k] = [int(i) for i in input().split()]
dic = collections.defaultdict(int)
for i in range(n):
  [a,b] = [int(j) for j in input().split()]
  dic[a] += b
keys = sorted(list(dic.keys()))
tmp = 0
for key in keys:
  tmp += dic[key]
  if k <= tmp:
    print(key)
    break
  
