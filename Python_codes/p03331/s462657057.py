n = int(input())

if n % 10:
    ans = 0
    while n > 0:
        ans += n % 10
        n = n //10
    print(ans)
else:
    print(10)
