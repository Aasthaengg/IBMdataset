N = int(input())
A = [int(input()) for i in range(N)]
import collections
c = collections.Counter(A)
#print(c)
ans = 0
for i in c:
  if c[i] % 2 != 0:
    ans += 1
print(ans)
