def main():
    x = int(input())
    if x <= 599:
        return 8
    elif x <= 799:
        return 7
    elif x <= 999:
        return 6
    elif x <= 1199:
        return 5
    elif x <= 1399:
        return 4
    elif x <= 1599:
        return 3
    elif x <= 1799:
        return 2
    return 1
print(main())
