import bisect
n = int(input())
a = list(map(int, input().split())); a.sort()
b = list(map(int, input().split())); b.sort()
c = list(map(int, input().split())); c.sort()
ab = [0 for i in range(n)]
ans = 0

for i in range(n):
  ab[i] = ab[i-1] + bisect.bisect_left(a, b[i])
for i in range(n):
  tmp = bisect.bisect_left(b, c[i])
  if tmp != 0:
  	ans += ab[tmp-1] 

print(ans)
