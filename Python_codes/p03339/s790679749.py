n=int(input())
s=input()
accuml=[0]*n
accumr=[0]*n
for i in range(1,n):
    accuml[i]+=accuml[i-1]
    accumr[n-i-1]+=accumr[n-i]
    if s[i-1]=="W":
        accuml[i]+=1
    if s[n-i]=="E":
        accumr[n-i-1]+=1
ans=10**18
for i in range(n):
    ans=min(ans,accuml[i]+accumr[i])
print(ans)
#print(accuml)
#print(accumr)