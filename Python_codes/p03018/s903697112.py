s=list(input())
S=[]
n=0
while n+1<len(s):
    if s[n:n+2]==["B","C"]:
        S.append("D")
        n+=1
    else:
        S.append(s[n])
    n+=1
a=0
ans=0
for i in range(len(S)):
    if S[i]=="D":
        ans+=a
    elif S[i]=="A":
        a+=1
    else:
        a=0
print(ans)