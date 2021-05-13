def actual(x):
    if x < 1200:
        return 'ABC'

    return 'ARC'

x = int(input())
print(actual(x))