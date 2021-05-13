x,y = map(int,input().split())
ans=0
while x*2**ans<=y: ans+=1
print(ans)