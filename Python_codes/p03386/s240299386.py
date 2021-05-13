import math
a , b , k = map(int , input().split())
ans = set()
for i in range(min(k , math.ceil((b - a + 1) / 2))):
  ans.add(a + i)
  ans.add(b - i)
ans = sorted(list(ans))
print('\n'.join([str(n) for n in ans]))