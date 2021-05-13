import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    """
    x = a+b
    y = b+c
    z = a+c
    """
    N, K = read_ints()
    answer = 0
    for a in range(1, N+1):
        complement = K-(a%K)
        if 2*complement%K == 0:
            if N-complement >= 0:
                answer += ((N-complement)//K+1)**2
    return answer


if __name__ == '__main__':
    print(solve())
