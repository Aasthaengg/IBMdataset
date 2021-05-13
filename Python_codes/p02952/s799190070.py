n = int(input())

if 1 <= n <= 9:
    print(n)
elif 10 <= n <= 99:
    print(9)
elif 100 <= n <= 999:
    print(9 + (n - 99))
elif 1000 <= n <= 9999:
    print(9 + 900)
elif 10000 <= n <= 99999:
    print(9 + 900 + (n - 9999))
else:
    print(9 + 900 + 90000)