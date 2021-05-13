n = int(input())
xs = [int(x) for x in input().split()]
xs.sort()

ans = xs[0]
for i in range(1,n):
  ans = (ans + xs[i]) / 2.

print(ans)
