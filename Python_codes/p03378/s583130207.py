n, m, x = map(int, input().split())
a = list(map(int, input().split()))

res1 = 0
res2 = 0
for i in a:
  if i<x:
    res1 += 1
  else:
    res2 += 1
    
print(min(res1, res2))