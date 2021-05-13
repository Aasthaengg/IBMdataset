n=int(input())
a=[]
for _ in range(n):
  a.append([int(i) for i in input().split()])
b=[0,0,0]
for i in range(n):
  minC=abs(a[i][1]-b[1])+abs(a[i][2]-b[2])
  if a[i][0]-b[0]<minC or (a[i][0]-b[0]-minC)%2==1:
    print("No")
    break
  b=a[i]
else:
  print("Yes")