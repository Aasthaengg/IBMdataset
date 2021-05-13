month, day = map(int, input().split())

if month <= day:
    print(month)
else:
    print(month - 1)