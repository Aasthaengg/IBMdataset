x = input()
s=0
ans=0
for i in x:
  if i == "S":
    s+=1
  else:
    if s==0:
      ans +=1
    else:
      s-=1
print(ans+s)