k, a, b = map(int, input().split())

if (b - a) < 2:
    ans = 1 + k

else:
    ans = a
    if (k-a-1) % 2 == 0:
        ans += (b - a) * int((k-a+1) / 2)
    else:
        ans += (b - a) * int((k-a) / 2) + 1

print(ans)
