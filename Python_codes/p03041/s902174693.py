n,k=map(int,input().split())
S=input()

s="ABCabc"
ans=[]
for i in range(len(S)):
    if i==k-1:
        ans.append(s[s.index(S[i])+3])
    else:
        ans.append(S[i])
print("".join(ans))
