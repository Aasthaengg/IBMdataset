n = int(input())
a = list(map(int,input().split()))
mi = a[0]
mii = 1
ma = a[0]
mai = 1
for i in range(n):
  if a[i] > ma:
    ma = a[i]
    mai = i+1
  if a[i] < mi:
    mi = a[i]
    mii = i+1
if mi >= 0:
  print(n-1)
  for i in range(1,n):
    print(i,i+1)
elif ma <= 0:
  print(n-1)
  for i in range(n,1,-1):
    print(i,i-1)
elif abs(ma) >= abs(mi):
  print(n*2-1)
  for i in range(n):
    print(mai,i+1)
  for i in range(1,n):
    print(i,i+1)
else:
  print(n*2-1)
  for i in range(n):
    print(mii,i+1)
  for i in range(n,1,-1):
    print(i,i-1)