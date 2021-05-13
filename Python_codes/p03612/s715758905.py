n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n-1):
  if i+1 == a[i]:
    a[i],a[i+1] = a[i+1],a[i]
    c += 1

if n == a[n-1]:
  c += 1
print(c)