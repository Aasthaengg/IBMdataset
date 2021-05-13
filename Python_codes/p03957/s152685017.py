s=input()

ans='No'
temp=''
for i in range(len(s)):
    if s[i]=='C':
        temp=s[i:]
        break
for i in temp:
    if i=='F':
        ans='Yes'
        break
        
print(ans)