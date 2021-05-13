s=input()
n=len(s)
o=[]
e=[]
for i in range(n):
    if (i+1)%2==0:
        e.append(s[i])
    else:
        o.append(s[i])
if o.count('L')==0 and e.count('R')==0:
    print('Yes')
else:
    print('No')