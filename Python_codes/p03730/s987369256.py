a, b, c = map(int, input().split())

ans = ''

if a % b == 0:
    if c == 0:
        ans = 'YES'
    else:
        ans = 'NO'
else:
    k = a % b
    for x in range(101):
        if (k * x) % b == c:
            ans = 'YES'
            break
    else:
        ans = 'NO'

print(ans)
