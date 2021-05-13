n = int(input())
if n%2 != 0:
    print(0)
else:
    ans = 0
    n = n//10
    ans += n
    while n > 0:
        n //= 5
        ans += n
    print(ans)