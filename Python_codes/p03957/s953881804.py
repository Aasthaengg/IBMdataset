s=input()
c=0
f=0
for i in range(len(s)):
    if s[i]=="C":
        if c==0:
            c=i+1
    if s[i]=="F":
        f=i+1
if c!=0 and c<f:
    print("Yes")
else:
    print("No")
