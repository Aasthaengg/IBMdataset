r, g, b, n = map(int,input().split())
ans = 0

for i in range(n+1):
    x = i*r
    if x > n:
        break
    for j in range(n+1):
        y = j*g
        z = n-x-y
        if x+y > n:
            break
        if z >= 0 and z%b == 0:
            ans += 1

print(ans)
