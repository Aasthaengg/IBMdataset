n = int(input())
x = [int(i) for i in input().split()]
c = []
for i,xi in enumerate(x):
  c.append(xi-i-1)
c.sort()
if n%2 == 1:
  b = c[n//2]
else:
  b = (c[n//2-1]+c[n//2])//2
ans = 0
for i in c:
  ans += abs(i-b)
print(ans)