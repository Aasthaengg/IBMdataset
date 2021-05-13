s=input()
ans=0
for index,i in enumerate(s):
  if index%2==0:
    if i=="p":
      ans-=1
  else:
    if i=="g":
      ans+=1
print(ans)