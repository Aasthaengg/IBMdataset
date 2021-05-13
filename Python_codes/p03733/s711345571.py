n,T = map(int,input().split())
t = list(map(int,input().split()))
pushtime = 0
ans = 0
for i in range(n):
    if n== 0:continue
    if pushtime+T > t[i]:
        ans+=t[i] - pushtime
        pushtime = t[i]
        
    
    else:
        ans +=T
        pushtime = t[i]
ans+=T
print(ans)
