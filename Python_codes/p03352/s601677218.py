x=int(input())
ans=0
for b in range(1,int(x**(1/2)+1)):
    for p in range(1,11):
        if b**p<=x and b**p>ans:
            ans=b**p
print(ans)