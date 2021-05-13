def function(x):
    base = 0
    for i in range(1, 10 ** 7):
        base *= 10
        base += 7
        base %= x
        if base == 0:
            return i

    return -1

x = int(input())
print(function(x))