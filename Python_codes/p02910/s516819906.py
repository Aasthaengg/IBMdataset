import sys
s=input()
l = len(s)
c=0
for i in range(l):
    if i%2==0:
        if s[i]=="R" or s[i]=="U" or s[i]=="D":
            continue
        else:
            c=1
            break
    if i%2==1:
        if s[i]=="L" or s[i]=="U" or s[i]=="D":
            continue
        else:
            c=1
            break
            
if c==1:
    print("No")
if c==0:
    print("Yes")