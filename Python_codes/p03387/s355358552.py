a, b, c = sorted(map(int, input().split()))
ans = 0
if (b - a) % 2 == 0:
    ans += ((b - a) // 2)
else:
    b += 1
    c += 1
    ans += 1
    ans += ((b - a) // 2)
ans += (c - b)
print(ans)