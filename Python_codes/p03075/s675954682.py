ans=0
a=[0]*5
for x in range(5):
  a[x]=int(input())
k=int(input())
for y in range(5):
  for z in range(5):
    if y!=z:
      if abs(a[y]-a[z])>k:
        ans+=1
if ans==0:
  print("Yay!")
else:
  print(":(")