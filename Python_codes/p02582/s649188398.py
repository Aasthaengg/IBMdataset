s=input()
c=0
tmp=0
for i in range(3):
    if s[i]=='R':
        tmp+=1
        if c<tmp:
            c=tmp
    else:
        tmp=0
print(c)