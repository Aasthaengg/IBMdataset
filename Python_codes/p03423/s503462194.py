n=int(input())
ans=0
j=0
for i in range(n):
    j+=1    
    if j==3:
        j=0
        ans+=1
print(ans)
