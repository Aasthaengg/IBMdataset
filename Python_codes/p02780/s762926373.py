n, k = map(int, input().split())
p = list(map(int, input().split()))
a = [0] * n 
asum = 0
for i in range(n):
  a[i] = (p[i]+1)/2 + asum
  asum = a[i]
ans = a[k-1]
for f in range(1, n-k+1):
  ans = max([ans, a[f+k-1] - a[f-1]])
print(ans)  