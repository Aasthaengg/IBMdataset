s=input()
b=s[0]
c=0
for a in s:
  if a!=b:
    c+=1
  b=a
print(c)