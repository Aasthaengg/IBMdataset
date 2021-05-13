s=input()
cnt=0
for i in range(len(s)):
  if s[i]=='0':
    cnt+=1
print(min(cnt,len(s)-cnt)*2)