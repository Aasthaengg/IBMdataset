[a,b]=list(map(int,input().split()))
ans=a+b
if ans>=24:
    ans-=24
print(ans)