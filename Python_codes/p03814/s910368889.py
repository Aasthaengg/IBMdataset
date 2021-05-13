s=input()
a,b=0,0
for i in range(len(s)):
  if s[i]=='A':
    a=i
    break
for j in range(len(s)-1,-1,-1):
  if s[j]=='Z':
    b=j
    break
print(len(s[a:b+1]))