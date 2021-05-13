a, b = map(int, input().split())


def answer(a: int, b: int) -> str:
    if (a * b) % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


print(answer(a, b))