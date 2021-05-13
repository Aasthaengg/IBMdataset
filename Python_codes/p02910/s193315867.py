s=input()
t=0
for i in range(len(s)):
    if i%2==0:
        if s[i]=="L":
            t+=1
    else:
        if s[i]=="R":
            t+=1
if t==0:
    print("Yes")
else:
    print("No")