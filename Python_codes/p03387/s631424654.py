a, b, c = sorted([int(i)for i in input().split()])
ans = 0
ma, mb, mc = [a % 2, b % 2, c % 2]

if ma == mb == mc:
    pass
elif ma != mb and mb == mc:
    b += 1
    c += 1
    ans += 1
elif ma == mc and ma != mb:
    a += 1
    c += 1
    ans += 1
elif ma == mb and mb != mc:
    a += 1
    b += 1
    ans += 1

ans += (c - b) // 2
ans += (c - a) // 2

print(ans)
