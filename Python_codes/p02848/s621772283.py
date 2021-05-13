N=int(input())
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
al=list(alphabet)
S=list(input())
ans=""
for i in range(len(S)):
    x=al.index(S[i])+N
    ans+=al[x%26]
print(ans)