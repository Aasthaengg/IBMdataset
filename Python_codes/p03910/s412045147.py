import sys

N=int(input())
temp=0
ans=[]
for i in range(1,N+1):
  temp+=i
  if temp==N:
    for j in range(1,i+1):
      print(j)
    else:
      sys.exit()
  elif temp>N:
    for j in range(1,i+1):
      if j==temp-N:
        continue
      print(j)
    else:
      sys.exit()
