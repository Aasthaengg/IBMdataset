import sys
n=int(input())
a=[int(input()) for i in range(n)]
for i in range(n):
  if a[i]>i:
    print(-1)
    sys.exit()
ct=0
for i in range(n-1,0,-1):
  if a[i]-1>a[i-1]:
    print(-1)
    sys.exit()
  elif a[i]-1==a[i-1]:
    ct+=1
  else:
    ct+=a[i]
print(ct)