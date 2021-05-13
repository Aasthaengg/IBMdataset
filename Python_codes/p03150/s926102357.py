s=input()
flag=False
ans='keyence'

for i in range(len(s)):
  for j in range(i,len(s)):
    if ans==s[:i]+s[j:]:
      flag=True
      break
if flag:
  print("YES")
else:
  print("NO")