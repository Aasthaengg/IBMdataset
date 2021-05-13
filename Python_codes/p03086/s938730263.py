s=input()
temp=0
ans=0
tar="ACGT"
for ch in s:
  if ch in tar:
    temp+=1
  else:
    ans=max(ans, temp)
    temp=0

print(max(ans,temp))


