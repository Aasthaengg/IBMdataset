X = int(input())

n = 0
if X <= 599:
    n = 8
elif X <= 799:
    n = 7
elif X <= 999:
    n = 6
elif X <= 1199:
    n = 5
elif X <= 1399:
    n = 4
elif X <= 1599:
    n = 3
elif X <= 1799:
    n = 2
elif X <= 1999:
    n = 1

print(n)