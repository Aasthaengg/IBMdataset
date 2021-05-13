s= input().strip()
l=len(s)
a=[]
z=[]
for i in range(l):
    if s[i]=='A':
        a.append(i)
    elif s[i]=='Z':
        z.append(i)
print(max(z)-min(a)+1)