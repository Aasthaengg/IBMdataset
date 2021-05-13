n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if sum(a)>sum(b):
  print("No")
else:
  ca = 0
  cb = 0
  for i in range(n):
    if a[i]>b[i]:
      cb += a[i]-b[i]
    else:
      ca += (b[i]-a[i]+1)//2
      cb += (b[i]-a[i])%2
  x = sum(b)-sum(a)
  if x >= ca and x >= cb and (x-ca)*2 == x-cb:
    print("Yes")
  else:
    print("No")