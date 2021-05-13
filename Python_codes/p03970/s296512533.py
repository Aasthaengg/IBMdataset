# coding: utf-8
s=input()
s_="CODEFESTIVAL2016"
ans=0
for i in range(len(s_)):
    if s[i]!=s_[i]:
        ans+=1
print(ans)