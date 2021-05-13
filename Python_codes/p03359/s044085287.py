month, day = [int(i) for i in input().split()]
if month > day:
    print(month - 1)
else:
    print(month)