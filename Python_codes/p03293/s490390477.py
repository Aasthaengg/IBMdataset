s=input()
t=input()
l=len(s)
ans=0
for i in range(l):
  ss=s[l-i:l]+s[0:l-i]
  if ss==t:
    print("Yes")
    break
else:
  print("No")