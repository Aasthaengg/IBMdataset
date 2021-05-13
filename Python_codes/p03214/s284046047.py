n = int(input())
a = list(map(int,input().split()))
avg = sum(a)/n
mi = sum(a)
ans = 0
for i in range(n):
  if mi > abs(avg-a[i]):
    mi = abs(avg-a[i])
    ans = i
print(ans)
