a,b=map(int,input().split())
ans=0
b=b*2+1
while a>0:
    a-=b
    ans+=1
print(ans)