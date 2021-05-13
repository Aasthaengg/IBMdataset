n = int(input())

if n <= 99:
    print(min(9, n))
elif n <= 9999:
    print(9 + min(900, n - 99))
elif n <= 999999:
    print(9 + 900 + min(90000, n - 9999))
