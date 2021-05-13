s=input()
l,d=[],[]
c=0
for i in s:
    if(i=='A'):
        l.append(c)
    if(i=='Z'):
        d.append(c)
    c+=1
print(max(d)-min(l)+1)
