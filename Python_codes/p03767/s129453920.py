n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
c = 0
t = 1
while t < 2*n:
  c += a[t]
  t += 2
print(c)
