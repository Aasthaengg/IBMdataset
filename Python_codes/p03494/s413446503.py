import sys
n=int(input())
a = list(map(int,input().split()))
b=0
while(True):
  for i in range(n):
    if(a[i]%2!=0):
      print(b)
      sys.exit()
    a[i]=a[i]//2
  b+=1
print(b)