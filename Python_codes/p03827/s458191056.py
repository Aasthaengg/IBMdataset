n=int(input())
s=str(input())
l=[0]
x=0
for i in range(0,len(s)):
    if(s[i]=='I'):
        x=x+1
        l.append(x)
    else:
        x=x-1
        l.append(x)
print(max(l))