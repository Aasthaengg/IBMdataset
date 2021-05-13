s=input()
p=s[0]
c=0
for x in s:
    if x!=p:
        c+=1
        p=x
print(c)