#
# 10a
#
import math


def main():
    x1, y1, x2, y2 = map(float, input().split())
    ret = math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
    print(f"{ret: .8f}")


if __name__ == '__main__':
    main()

