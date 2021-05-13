r, g, b, n = map(int,input().split())

ans = 0
for i in range(0,n+1):
    for j in range(0,n-i+1):
        if r*i+g*j > n:
            break
        if (n-r*i-g*j)%b == 0:
            ans += 1
print(ans)