s=input()
cnt=[0]*len(s)
for i in range(len(s)):
  if s[i]=='A' or s[i]=='T' or s[i]=='C' or s[i]=='G':
    if i==0:
      cnt[0]=1
    else:
      cnt[i]=cnt[i-1]+1
print(max(cnt))