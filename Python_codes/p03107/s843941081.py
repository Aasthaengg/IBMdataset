s = input()
a,b=0,0
for si in s:
  if si=="1":
    b+=1
  else:
    a+=1
print(2*min(a,b))