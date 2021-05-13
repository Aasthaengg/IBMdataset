mod = 10**9 + 7
n = int(input())
a = sorted(list(map(int,input().split())))
 
if n % 2 == 0:
  for i in range(n//2):
    if not a[2*i] == a[2*i+1] == 2*i+1:
      print(0)
      exit()
else:
  if a[0] != 0:
    print(0)
    exit()
  for i in range(n//2):
    if not a[2*i+1] == a[2*i+2] == 2*i+2:
      print(0)
      exit()
print(pow(2, n//2) % mod)