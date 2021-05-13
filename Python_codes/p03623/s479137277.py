def actual(x, a, b):
    # すぬけ君の位置から店A,B までの距離は異なる

    if abs(x - a) < abs(x - b):
        return 'A'

    return 'B'

x, a, b = map(int, input().split())
print(actual(x, a, b))