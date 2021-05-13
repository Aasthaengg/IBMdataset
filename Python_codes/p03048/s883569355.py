r, g, b, n = map(int, input().split())
ans = 0
for i in range(n//r+1):
    for j in range(n//g+1):
        nn = n - r*i - g*j
        if nn < 0:
            break
        if nn % b == 0:
            ans += 1
print(ans)
