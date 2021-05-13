s=input()
a='CODEFESTIVAL2016'
ans=0
for i in range(len(s)):
    ans+=1 if s[i]!=a[i] else 0
print(ans)