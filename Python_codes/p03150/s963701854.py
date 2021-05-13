S=input()
n=len(S)
ans="NO"
for i in range(n):
  for j in range(i,n):
    if S[:i]+S[j:]=="keyence":
      ans="YES"
      break
print(ans)
