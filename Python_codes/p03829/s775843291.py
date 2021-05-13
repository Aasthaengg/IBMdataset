n,a,b = map(int, input().split())
x = list(map(int, input().split()))
d = [0] * (n-1)
for i in range(n-1):
  d[i] = min(b,a * (x[i+1]-x[i]))
  
print(sum(d))
