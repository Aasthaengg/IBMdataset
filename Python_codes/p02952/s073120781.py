n = int(input())
ans = 0

if n >= 10000:
    ans += n - 9999
    ans += 909
    if n == 100000:
        ans -= 1
    print(ans)
    exit()

if n >= 100:
    ans += n - 99
    ans += 9
    if n >= 1000:
        ans -= n-999
    print(ans)
    exit()

if n > 9:
    print(9)
    exit()

print(n)