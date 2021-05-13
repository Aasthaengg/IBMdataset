import sys
a=[0]*5
a[0]=int(input())
a[1]=int(input())
a[2]=int(input())
a[3]=int(input())
a[4]=int(input())
k=int(input())
for i in range(5):
  for j in range(i+1,5):
    if a[j]-a[i]>k :
      print(":(")
      sys.exit()
print("Yay!")