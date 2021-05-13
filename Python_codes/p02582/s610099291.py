s=input()
flag=False
ans=0
for i in range(3):
    if s[i]=="R":
        ans+=1
        if not flag:
            flag=True
    if s[i]=="S" and flag:
        break
print(ans)