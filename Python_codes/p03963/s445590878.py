
n, k = map(int, input().strip().split())


def func(balls, colors):
    combination = colors * (colors - 1) ** (balls - 1)
    print(combination)


func(balls=n, colors=k)
