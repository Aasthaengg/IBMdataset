n = int(input())
a = sorted(list(map(int, input().split())))

if n == 1:
  print(1)
  exit()
elif n%2 == 0:
  for i in range(0,n-2,2):
    if a[i] != a[i+1] or a[i] == a[i+2]:
      print(0)
      exit()
  if a[-2] != a[-1]:
    print(0)
    exit()
else:
  if a[0] != 0 or a[1] == 0:
    print(0)
    exit()
  for i in range(1,n-2,2):
    if a[i] != a[i+1] or a[i] == a[i+2]:
      print(0)
      exit()
  if a[-2] != a[-1]:
    print(0)
    exit()

mod = 10**9+7
if n%2 == 0: print(2**(n//2)%mod)
else: print(2**((n-1)//2)%mod)