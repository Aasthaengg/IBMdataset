n = int(input())

ans = (n // 11) * 2

rem = n % 11

if rem > 0 :
    if rem <= 6:
        ans += 1
    else:
        ans += 2

print(ans)
