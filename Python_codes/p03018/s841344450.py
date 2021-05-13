s=list(input())
x=[]
for i in range(len(s)):
    if s[i]=='A':
        x.append(0)
    elif s[i]=='B':
        x.append(1)
    elif i>0 and s[i]=='C' and s[i-1]=='B':
        x[-1]=3
    else:
        x.append(2)
ans=0
tmp0=0
for i in range(len(x)):
    if x[i]==0:
        tmp0+=1
    if x[i]==3:
        ans+=tmp0
    if x[i]!=0 and x[i]!=3:
        tmp0=0
print(ans)