n=int(input())
import collections
D=collections.defaultdict(int)
for i in range(n):
  p=int(input())
  D[p]=D[p-1]+1
print(n-max(list(D.values())))