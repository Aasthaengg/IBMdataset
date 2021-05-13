def answer(a: int, b: int) -> str:
    if a == b:
        return 'EQUAL'

    if a < b:
        return 'LESS'

    if a > b:
        return 'GREATER'


def main():
    a = int(input())
    b = int(input())
    print(answer(a, b))


if __name__ == '__main__':
    main()