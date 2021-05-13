n= int(input())
a=[int(i) for i in input().split()]
ans = 0
for i in range(1,n):
  add = max(0, a[i-1]-a[i])
  ans += add
  a[i] += add
print(ans)