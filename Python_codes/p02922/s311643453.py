a,b=map(int,input().split())
ans,num=0,1
while num<b:
    num-=1
    num+=a
    ans+=1
print(ans)