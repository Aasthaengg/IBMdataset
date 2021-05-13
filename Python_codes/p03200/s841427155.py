S=list(str(input()))
c=0
ans=0
for i in S:
  if i=="B":
    c+=1
  else:
    ans+=c
print(ans)