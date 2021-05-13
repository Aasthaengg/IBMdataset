n = int(input())
a = list(map(int, input().split()))

a.sort()

c = 0
s = []
for i in range(n):
  c+=a[i]
  s.append(c)
ng = 0
for i in range(1,n):
  if a[i] > 2*s[i-1]:
    ng = i
print (n-ng)