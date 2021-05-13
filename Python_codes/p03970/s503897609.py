s="CODEFESTIVAL2016"
l=input()
cnt=0
for a in range(len(s)):
  if s[a]!=l[a]:
    cnt+=1
print(cnt)