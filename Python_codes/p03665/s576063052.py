n,p = map(int, input().split())
a = list(map(int, input().split()))

odd = 0
even = 0

for i in range(n):
  if a[i]%2 == 0:
    even += 1
  else:
    odd += 1

if odd == 0:
  if p == 1:
    print(0)
  else:
    print (2**n)
else:
  print (2**(n-1))