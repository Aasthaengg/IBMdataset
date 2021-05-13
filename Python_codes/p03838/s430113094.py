x, y = map(int, input().split())
if x <= y:
    ans = min(y-x, abs(abs(x)-abs(y))+1)
else:
    ans = abs(abs(y) - abs(x))
    if x * y > 0:
        ans += 2
    else:
        ans += 1
print(ans)