s=input()
t=input()
c=0
for i in range(len(s)):
    if s[i:]+s[0:i]==t:
        c+=1
        break
if c>0:
    print('Yes')
else:
    print('No')