n=int(input())
h=[int(x) for x in input().split()]
a=1
for i in range(n-1):
  if h[i]>h[i+1]:
    h[i+1]+=1
    if h[i]>h[i+1]:
      print("No")
      a=0
      break
if a==1:
  print("Yes")