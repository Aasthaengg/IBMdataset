s=input()
ct=0
ans=0
flag=0
for i in range(len(s)):
    if (flag==0)and(s[i]=='A'):
        flag=1
    elif (flag==1):
        ct+=1
    if (flag==1)and(s[i]=='Z'):
        ans=ct
print(ans+1)

