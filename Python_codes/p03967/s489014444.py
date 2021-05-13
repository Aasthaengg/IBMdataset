s=input()
c=0
for i in range(len(s)):
  if i%2:
    c+=(s[i]=='g')
  else:
    c-=(s[i]=='p')
print(c)