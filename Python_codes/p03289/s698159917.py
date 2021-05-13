s=input()
n=len(s)
if s[0]!="A":
    print("WA")
    exit()
if all(s[i]!="C" for i in range(2,n-1)):
    print("WA")
    exit()
f=0
for i in range(n):
    if s[i]==s[i].upper():
        f+=1
print("AC" if f==2 else "WA")
    
    
