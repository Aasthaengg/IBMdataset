x=int(input())
ans=1
for a in range(2,1000):
    p=2
    while a**p<=x:
        ans=max(ans,a**p)
        p+=1
print(ans)
