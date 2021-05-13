a=input()
ans=0
for i in range(0,len(a)-1):
    if a[i]!=a[i+1]:
        ans+=1
print(ans)