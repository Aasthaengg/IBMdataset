l=[]
for i in range(5):
  a=int(input())
  l.append(a)
l.sort()
k=int(input())
if k>=l[4]-l[0]:
  print("Yay!")
else:
  print(":(")
