n , t = map(int,input().split())
z = list(map(int,input().split()))
ans = 0
for i in range(1,n):
    if z[i-1] + t <= z[i]:
        ans += t
    elif z[i-1] + t > z[i]:
        ans += z[i] - z[i-1]
        
ans += t

print(ans)