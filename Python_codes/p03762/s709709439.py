n, m = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
w = 0
for i in range(1, n):
  w += i*(n-i)*(xs[i]-xs[i-1])
h = 0
for i in range(1, m):
  h += i*(m-i)*(ys[i]-ys[i-1])
r = w*h%1000000007
print(r)
