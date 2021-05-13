from collections import defaultdict
n = int(input())
p = defaultdict(int)
for i in range(1,n+1):
  j = int(str(i)[0])
  k = int(str(i)[-1])
  p[(j,k)] += 1
ans = 0
for j in range(10):
  for k in range(10):
    ans += p[(j,k)]*p[(k,j)]
print(ans)