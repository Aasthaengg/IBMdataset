n = int(input())

if n % 2 == 1:
    print(0)
    exit()

elif n % 2 == 0:
    ans = 0
    t = 10
    while n >= t:
        ans += n // t
        t *= 5
    print(ans)
