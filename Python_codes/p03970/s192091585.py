N=input()
s='CODEFESTIVAL2016'
ans=0
for i in range(16):
    if not N[i]==s[i]:ans+=1
print(ans)