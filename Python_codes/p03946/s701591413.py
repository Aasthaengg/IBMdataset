n,t = map(int,input().split())
a =list(map(int,input().split()))
MIN = float("inf")
b = [0] * n
for i in range(n):
  MIN = min(MIN,a[i])
  b[i] = a[i]-MIN
print(b.count(max(b)))
