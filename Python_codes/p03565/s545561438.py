S=list(input())
T=input()
start=-1
ans=[]
for i in range(len(S)):
    flag=0
    for j in range(len(T)):
        if i+j>=len(S):
            flag=1
            break
        if S[i+j]==T[j] or S[i+j]=="?":
            continue
        else:
            flag=1
            break
    if flag==0:
        start=max(start,i)
for i in range(start,start+len(T)):
    S[i]=T[i-start]
for i in range(len(S)):
    if S[i]=="?":
        ans.append("a")
    else:
        ans.append(S[i])
if start==-1:
    print("UNRESTORABLE")
else:
    print("".join(ans))