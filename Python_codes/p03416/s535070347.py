a,b=map(int,input().split())
ans=0
for i in range(a,b+1):
    if i%10==i//10000 and i//10%10==i//1000%10:ans+=1
print(ans)