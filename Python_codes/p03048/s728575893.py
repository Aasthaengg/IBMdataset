r, g, b, n = map(int,input().split())
ans = 0
x = n//min(r,g,b)

for i in range(x+1):
    for j in range(x+1):
        y = r*i + g*j
        if n-y >= 0 and (n-y)%b == 0:
            ans += 1

print(ans)