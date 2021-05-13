S=input()
temp=0
ans=0
ACGT=["A","C","G","T"]
for i in range(len(S)):
    if S[i] in ACGT:
        temp+=1
    else:
        if temp>ans:
            ans=temp
        temp=0
if temp>ans:
    ans=temp
print(ans)
