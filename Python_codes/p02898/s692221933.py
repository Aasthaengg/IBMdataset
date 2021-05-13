n,k = map(int,input().split())
ans = 0
for h in map(int,input().split()):
    ans += (h>=k)
print(ans)