import math
import sys


def main():
    sx, sy, tx, ty = map(int, input().split())
    dx = tx - sx
    dy = ty - sy
    ax11 = [("R" if dx >= 0 else "L")] * abs(dx)
    ay11 = [("U" if dy >= 0 else "D")] * abs(dy)
    ax12 = [("L" if dx >= 0 else "R")] * abs(dx)
    ay12 = [("D" if dy >= 0 else "U")] * abs(dy)
    ax21 = [("D" if dy >= 0 else "U")] * 1 + \
        [("R" if dx >= 0 else "L")] * (abs(dx) + 1)
    ay21 = [("U" if dy >= 0 else "D")] * (abs(dy) + 1) + \
        [("L" if dx >= 0 else "R")] * 1
    ax22 = [("U" if dy >= 0 else "D")] * 1 + \
        [("L" if dx >= 0 else "R")] * (abs(dx) + 1)
    ay22 = [("D" if dy >= 0 else "U")] * (abs(dy) + 1) + \
        [("R" if dx >= 0 else "L")] * 1
    a1 = "".join(ax11 + ay11 + ax12 + ay12)
    a2 = "".join(ax21 + ay21 + ax22 + ay22)
    print(a1 + a2)


if __name__ == '__main__':
    main()
