s=input()
n=len(s)
ans=0
for i in range(n):
    for j in range(i,n):
        if all('ACGT'.count(c)==1 for c in s[i:j+1]):
            ans=max(ans,len(s[i:j+1]))
print(ans)