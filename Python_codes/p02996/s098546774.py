n=int(input())
a=[]
for i in range(n):
  a.append(list(map(int,input().split())))

import sys

a.sort(key=lambda x: x[1])
sum=a[0][0]
for i in range(n-1):
  if sum>a[i][1]:
    print("No")
    sys.exit()
  sum=sum+a[i+1][0]
if sum>a[n-1][1]:
  print("No")
  sys.exit()
print("Yes")
  
  
