import numpy as np
import math

N, H = 2, 10
ARR = [
    [3, 5],
    [2, 6]
]

N, H = 4, 1000000000
ARR = [
    [1, 1],
    [1, 10000000],
    [1, 30000000],
    [1, 99999999]
]

N, H = 5, 500
ARR = [
    [35, 44],
    [28, 83],
    [46, 62],
    [31, 79],
    [40, 43]
]

N, H = map(int, input().split())
ARR = [list(map(int,input().split())) for i in range(N)]


def calculate(n, h, arr):
    arr = np.array(arr)
    A1 = arr[:, 0]
    B1 = arr[:, 1]

    largestA1 = max(A1)

    b2 = sorted(B1, key=lambda x: -x)

    result = 0
    for i in range(len(b2)):

        if h <= 0:
            break
        if b2[i] >= largestA1:
            h = h - b2[i]
            result += 1
        else:
            break

    if h > 0:
        result += math.ceil(h / largestA1)

    return result


res = calculate(N, H, ARR)
print(res)
