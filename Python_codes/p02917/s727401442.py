n = int(input())
b = list(map(int,input().split()))
a = [0]*n
ans = 0

a[0] = b[0]
a[n-1] = b[n-2]
for i in range(1,n-1):
  a[i]=min(b[i-1],b[i])
for j in range(n):
  ans += a[j]

print(ans)