import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    N = read_int()
    answer = 0
    INF = 10**10
    XL = []
    for i in range(N):
        XL.append(read_ints())
    XL.sort(key=lambda xl: xl[0]+xl[1])
    current = -INF
    for x, l in XL:
        if x-l >= current:
            answer += 1
            current = x+l
    return answer


if __name__ == '__main__':
    print(solve())
