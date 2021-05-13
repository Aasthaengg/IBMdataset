n = int(input())
a = 0
if 400 <= n <= 599:
    a = 8
elif 600 <= n <= 799:
    a = 7
elif 800 <= n <= 999:
    a = 6
elif 1000 <= n <= 1199:
    a = 5
elif 1200 <= n <= 1399:
    a = 4
elif 1400 <= n <= 1599:
    a = 3
elif 1600 <= n <= 1799:
    a = 2
else:
    a = 1
print(a)