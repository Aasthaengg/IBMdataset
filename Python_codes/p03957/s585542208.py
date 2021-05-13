c=False
f=False
s=input()
for i in s:
    if i=="C":
        c=True
    if i=="F" and c==True:
        f=True

if c and f:
    print("Yes")
else:
    print("No")