n=int(input())
da=list(map(int,input().split()))
co=0
no=-1
ko=0
ans=0
while co<n:
    if no==da[co]:
        ko+=1
    else:
        ans+=ko//2
        no=da[co]
        ko=1
    co+=1
ans+=ko//2
print(ans)
    
