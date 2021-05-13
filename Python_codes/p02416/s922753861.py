while True:
    n = int(input())
    if n == 0:
        break
    r = 0
    while n != 0:
        r += n%10
        n //= 10
    print(r)    