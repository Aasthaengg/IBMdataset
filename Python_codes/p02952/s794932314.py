n = int(input())

if n < 10:
    print(n)
elif 10 <= n < 100:
    print(9)
elif 100 <= n < 1000:
    print(9+(n-99))
elif 1000 <= n < 10000:
    print(9+900)
elif 10000 <= n < 100000:
    print(9+900+(n-9999))
elif 100000 <= n:
    print(9+900+90000)