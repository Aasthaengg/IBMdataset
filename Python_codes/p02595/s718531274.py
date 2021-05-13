n, d = list(map(int, input().split()))
ans = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    val = ((x**2)+(y**2))**(1/2)
    if val <= d:
        ans += 1 
        
print(ans)