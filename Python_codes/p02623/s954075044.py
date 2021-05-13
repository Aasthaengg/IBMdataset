import numpy as np
import bisect
from typing import List


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(t(n, m, k, a, b))


def t(n: int, _: int, k: int, a: List[int], b: List[int]) -> int:
    a = np.concatenate([[0], a])
    a = np.cumsum(a)
    b = np.concatenate([[0], b])
    b = np.cumsum(b)

    ret = 0
    for i in range(n + 1):
        x = a[i]
        s = k - x
        if s < 0:
            break
        j = bisect.bisect(b, s) - 1
        ret = max(ret, i + j)

    return ret


if __name__ == '__main__':
    main()
