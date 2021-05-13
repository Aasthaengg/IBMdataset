n=int(input())
l_b=2
l=1
if n==0:
  print("2")
elif n==1:
  print("1")
else:
  for i in range(2,n+1):
    l_bb=l_b
    l_b=l
    l=l_b+l_bb
  print(l)