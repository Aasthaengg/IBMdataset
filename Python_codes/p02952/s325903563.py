n = int(input())

if n <= 99:
    print(min(n, 9))
elif 100 <= n <= 9999:
    print(9 + ((min(n, 999)) - 99))
else:
    print(9 + 900 + min(n, 99999) - 9999)
