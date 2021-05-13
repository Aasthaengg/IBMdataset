s=input()
ans=0
for i in range(4):
    for j in range(4):
        if s[i]==s[j]:
            ans+=1
        else:
            pass
if ans==8:
    print("Yes")
else:
    print("No")