import math
N = int(input())
K = list(map(int,input().split()))
hashmap = {}
for k in K:
  if k not in hashmap:
    hashmap[k] = 0
  hashmap[k]+=1
total = 0
for v in hashmap.values():
  if v>=2:
  	total+=math.factorial(v) // (math.factorial(v - 2) * 2)

for k in K:
  print(total-(hashmap[k]-1))