s=input()
a=s[0]
c=0
for i in range(1,len(s)):
  if s[i]!=a:
    c+=1;a=s[i]
print(c)