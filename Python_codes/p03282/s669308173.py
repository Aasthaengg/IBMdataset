s=input()
k=int(input())
t=0
one=0
for i in s:
  if i=="1":
    one+=1
  else:
    t=i
    break
if k<=one:
  print(1)
else:
  print(t)