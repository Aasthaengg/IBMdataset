x=input()
a=0
ans=0
for i in range(len(x)):
  if x[i]=="T":
    a=a+1
    if a>ans:
      ans=a
  else:
    a=a-1
print(ans*2)