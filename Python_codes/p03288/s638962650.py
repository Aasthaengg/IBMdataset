def actual(r):
    if 0 <= r < 1200:
        return 'ABC'

    if 1200 <= r < 2800:
        return 'ARC'

    return 'AGC'

r = int(input())
print(actual(r))