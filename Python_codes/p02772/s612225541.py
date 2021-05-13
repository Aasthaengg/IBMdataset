n=int(input())
list=[[0]*n]
list=input().split()
g=0
c=0
for i in range(n):
  list[i]=int(list[i])
  if list[i]%2==0:
    g+=1
    if list[i]%3==0 or list[i]%5==0:
      c+=1
if g==c:
  print("APPROVED")
else:
  print("DENIED")
  
