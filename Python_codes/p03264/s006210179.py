n = int(input())
if n % 2 == 0:
    n //= 2
    print(n * n)
else:
    a = n // 2
    print(a * (n-a))