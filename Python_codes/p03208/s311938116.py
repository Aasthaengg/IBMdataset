n,k=map(int,input().split())
a = [int(input()) for i in range(n)]
a = sorted(a)
min_ = 10**18
for i in range(n-k+1):
  min_ = min(min_, a[i+k-1]-a[i])
print(min_)