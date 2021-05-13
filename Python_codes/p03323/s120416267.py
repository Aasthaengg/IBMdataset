def actual(a, b):
    if a >= 9 or b >= 9:
        return ':('

    return 'Yay!'

a, b = map(int, input().split())
print(actual(a, b))