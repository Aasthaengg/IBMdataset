N=int(input())
a=list(map(int,input().split()))

ans=0
x=a[0]
length=1

for ai in a[1:]:
    if ai==x:
        length+=1
    else:
        ans+=length//2
        x=ai
        length=1
ans+=length//2

print(ans)