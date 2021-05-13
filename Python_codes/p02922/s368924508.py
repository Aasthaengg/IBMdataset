a,b = map(int,input().split())
ans = (b-1)//(a-1)
if (b-1)%(a-1) :
    ans+=1
print(ans)