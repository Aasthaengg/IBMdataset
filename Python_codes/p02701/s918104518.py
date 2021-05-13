from collections import defaultdict
n=int(input())
d=defaultdict(int)

for x in range(n):
  d[input()]+=1
  
print(len(d))