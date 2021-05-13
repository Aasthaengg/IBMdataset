x, y = map(int, input().split())

ans = 10000000000
if y >= x:
    ans = min(ans, y-x)
if y >= -x:
    ans = min(ans, y+x+1)
if -y >= x:
    ans = min(ans, 1-x-y)
if -y >= -x:
    ans = min(ans, x-y+2)
print(ans)