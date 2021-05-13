n=int(input())
m=0
l=0
for i in range(n):
  A,B=map(int,input().split())
  if (A==B):
    m+=1
  else:
    m=0
  if (m==3):
    print("Yes")
    l=1
    break

if (l==0):
  print("No")