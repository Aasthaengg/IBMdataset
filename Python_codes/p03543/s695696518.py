n=input()
ans=0
for i in range(2):
  if n[i]==n[i+1]==n[i+2]:
    ans+=1
if ans==0:
  print("No")
else:
  print("Yes")