s=input()
ans=0
if s[0]!='A':
    print("WA")
    exit()
for i in range(1,int(len(s))):
    if s[i].isupper():
        if i==1 or i==int(len(s))-1 or s[i]!='C':
            print("WA")
            exit()
        ans+=1
if ans !=1:
    print("WA")
    exit()
print("AC")