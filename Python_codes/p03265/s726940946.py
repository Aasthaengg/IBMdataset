from typing import List


def answer(x1: int, y1: int, x2: int, y2: int) -> List[int]:
    x = x2 - x1
    y = y2 - y1

    x3 = x2 - y
    y3 = y2 + x
    x4 = x1 - y
    y4 = y1 + x

    return [x3, y3, x4, y4]


def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = answer(x1, y1, x2, y2)
    print(x3, y3, x4, y4)


if __name__ == '__main__':
    main()
