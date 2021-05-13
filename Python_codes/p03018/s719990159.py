s=input().replace("BC","X")
ans=0
acc=0
for i in range(len(s)):
    if s[i]=="B" or s[i]=="C":
        acc=0

    elif s[i]=="A":
        acc+=1
    elif s[i]=="X":
        ans+=acc


print(ans)