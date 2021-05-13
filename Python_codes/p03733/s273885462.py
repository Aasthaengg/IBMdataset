n,t = map(int, input().split())
a = [int(i) for i in input().split()]

ans = 0

for i in range(0,n-1):
  ans+=(min(t, a[i+1]-a[i]))
print(ans+t)