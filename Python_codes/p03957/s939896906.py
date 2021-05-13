s=input()
ans="No"
flag=False
for i in range(len(s)):
  if not flag and s[i]=="C":
    flag=True
  elif flag and s[i]=="F":
    ans="Yes"
    break
print(ans)
