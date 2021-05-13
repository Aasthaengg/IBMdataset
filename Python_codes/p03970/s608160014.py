s=input()
org="CODEFESTIVAL2016"

cnt=0
for i in range(len(s)):
  if s[i]!=org[i]:
    cnt+=1
print(cnt)