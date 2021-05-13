S=input()
l=len(S)
ans=0
str='ACGT'
for i in range(l):
    for j in range(i,l):
        if all (str.count(x)==1 for x in S[i:j+1]):
            ans=max(ans,j-i+1)
print(ans)