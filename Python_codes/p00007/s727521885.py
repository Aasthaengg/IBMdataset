import sys

for line in sys.stdin:
    n = int(line)
    debt = 100000
    for k in range(n):
        debt *= 1.05
        if debt / 1000 - int(debt) / 1000 > 0:
            debt = (int(debt) / 1000 + 1) * 1000
        else:
            debt = int(debt)
    print debt