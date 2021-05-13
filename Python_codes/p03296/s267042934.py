from itertools import groupby

n = int(input())
ans = 0
for key, elems in groupby(map(int,input().split())):
  num = len(list(elems))
  if num >= 2: ans += num//2
print(ans)