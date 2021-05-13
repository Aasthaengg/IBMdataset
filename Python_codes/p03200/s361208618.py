s=input()
n=len(s)
tmp=0
ans=0
for i in range(n):
    if s[i]=="W":
        ans+=i-tmp
        tmp+=1
print(ans)