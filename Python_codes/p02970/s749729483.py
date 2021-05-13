n, d = map(int, input().split())
x = 1
ans = 0
while x <= n:
    x = x + (2*d+1)
    ans += 1
print(ans)
