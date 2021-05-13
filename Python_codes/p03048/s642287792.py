r, g, b, n = map(int, input().split())
ans = 0
for i in range(0, n+1):
    for j in range(0, n-i+1):
        check = (n-(i*r + j*g))/b
        if check % 1 == 0 and check >= 0:
            ans += 1
print(ans)
