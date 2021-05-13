
def resolve():
    S = int(input())

    x1, y1 = 0, 0
    x2, y2 = 1, 10 ** 9

    x3 = (S + y2 - 1) // y2
    y3 = x3 * y2 - S

    print(x1, y1, x2, y2, x3, y3)


if __name__ == "__main__":
    resolve()
