s=input()
if "keyence"==s:exit(print("YES"))
for i in range(10):
  for j in range(i,len(s)):
    if s[:i]+s[j:]=="keyence":exit(print("YES"))
print("NO")
