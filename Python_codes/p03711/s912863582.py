x, y = map(int, input().split())


def group(n):
    if n in [1, 3, 5, 7, 8, 10, 12]:
        return 1
    elif n in [4, 6, 9, 11]:
        return 2
    else:
        return 3


print("Yes" if group(x) == group(y) else "No")