# AOJでnumpyが使えないから自力で内積を求める
import sys
# import numpy as np
import math

input = sys.stdin.readline
n = int(input())
# ベクトルの60度回転で使う
cos60 = math.cos(math.radians(60))
sin60 = math.sin(math.radians(60))
# k = np.array([[cos60, -(sin60)], [sin60, cos60]])
k = ([[cos60, -(sin60)], [sin60, cos60]])


def main():
    start = [0.00000000, 0.00000000]
    end = [100.00000000, 0.00000000]
    print(' '.join(map(str, start)))
    Koch(start, end, 0)
    print(' '.join(map(str, end)))


def Koch(start, end, layer):
    layer += 1
    if layer > n:
        return
    point1 = [((end[0] - start[0]) / 3) + start[0], ((end[1] - start[1]) / 3) + start[1]]
    Koch(start, point1, layer)
    print(' '.join(map(str, point1)))
    point3 = [((end[0] - start[0]) / 3 * 2) + start[0], ((end[1] - start[1]) / 3 * 2) + start[1]]
    # vec = np.array([[point3[0] - point1[0]], [point3[1] - point1[1]]])  # vecは一旦原点に戻す
    vec = ([[point3[0] - point1[0]], [point3[1] - point1[1]]])  # vecは一旦原点に戻す
    point2 = [[k[0][0] * vec[0][0] + k[0][1] * vec[1][0]], [k[1][0] * vec[0][0] + k[1][1] * vec[1][0]]]  # 内積をとって60度左回転する
    point2 = [point2[0][0] + point1[0], point2[1][0] + point1[1]]  # 元あった点に戻す
    Koch(point1, point2, layer)
    print(' '.join(map(str, point2)))
    Koch(point2, point3, layer)
    print(' '.join(map(str, point3)))
    Koch(point3, end, layer)


if __name__ == '__main__':
    main()

