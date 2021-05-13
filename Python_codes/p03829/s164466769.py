n,a,b=map(int,input().split())
x = list(map(int,input().split()))
ans = 0
for i in range(n-1):
    walk_i = (x[i+1] - x[i])*a
    tel_i = b
    ans+=min(walk_i,tel_i)
print(ans)
