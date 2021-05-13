from collections import Counter
from typing import List


def main(n: int, a: List[int]):
    c = Counter(a)
    ans = 0

    for t in c.values():
        if t % 2 == 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    n = int(input())
    a = [int(input()) for _ in range(n)]

    main(n, a)
