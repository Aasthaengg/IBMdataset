a,b,c = map(int, input().split())

ans=b*2
ans+=a+1
ans = min(ans,b+c)
print(ans)