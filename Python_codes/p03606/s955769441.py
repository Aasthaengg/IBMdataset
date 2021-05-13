ans=0
for i in range(int(input())):
    l,r=map(int,input().split())
    ans+=r+1-l
print(ans)