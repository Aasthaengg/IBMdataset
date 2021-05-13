S=input()
ans=0
a=0
for i in range(len(S)):
    if S[i]=="A":
        if i>0 and S[i-1]=="B":
            a=0
        a+=1
    elif S[i]=="B":
        if i>0 and S[i-1]=="B":
            a=0
    elif S[i]=="C":
        if i>0 and S[i-1]=="B":
            ans+=a
        else:
            a=0
print(ans)