n,m = map(int,input().split())
query = [list(map(lambda x:int(x)-1,input().split())) for i in range(m)]
query.sort(key=lambda x:x[1])

l_end = -1
ans = 0
for i in range(m):
    a,b = query[i]
    if a>=l_end:
        l_end = b
        ans+=1
print(ans)