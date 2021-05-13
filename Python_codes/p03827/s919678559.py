n=int(input())
s=input()
cnti=0
cntd=0
ans=0
for i in range(n):
    if s[i]=='I':
        cnti+=1
    if s[i]=='D':
        cntd+=1
    ans=max(ans,cnti-cntd)
print(ans)