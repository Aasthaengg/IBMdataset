n,d = map(int,input().split())
ans = 0
for _ in range(n) :
    x,y = map(int,input().split())
    distance = (x**2 + y**2)**0.5
    if distance <= d :
        ans += 1
print(ans)