S=input()
T=input()

LS=len(S)
LT=len(T)

ans=[]
for i in range(LS-LT+1):
    F=True
    for t in range(LT):
        if T[t]==S[i+t] or S[i+t]=="?":continue
        else:
            F=False
            break
    if F:
        temp=""
        for j in range(LS):
            if j<i and S[j]=="?":
                temp+="a"
            elif i<=j<i+LT:
                temp+=T[j-i]
            elif j>=i+LT and S[j]=="?":
                temp+="a"
            else:
                temp+=S[j]
        ans.append(temp)

if len(ans)==0:
    print("UNRESTORABLE")
else:
    ans.sort()
    print(ans[0])
