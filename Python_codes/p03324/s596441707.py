d, n = map(int, input().split())

if d > 0:
    ans = 100**d*n
    if n == 100:
        ans = 100**d*101
else:
    ans = n
    if n == 100:
        ans = 101

print(ans)