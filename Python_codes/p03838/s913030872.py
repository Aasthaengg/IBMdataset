a, b = map(int, input().split())

if a * b > 0:
    ans = abs(b - a)
    if a > b:
        ans += 2

else:
    ans = abs(a - b)
    if a > b:
        ans += 1
    tmp = abs(abs(a) - abs(b)) + 1
    ans = min(ans, tmp)
    
print(ans)