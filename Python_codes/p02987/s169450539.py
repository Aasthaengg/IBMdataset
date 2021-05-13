s=str(input())
s2=[]
a=0
for i in range(4):
    if s[i] in s2:
        a+=1
    else:
        s2.append(s[i])
if a==2 and len(s2)==2:
    print("Yes")
else:
    print("No")