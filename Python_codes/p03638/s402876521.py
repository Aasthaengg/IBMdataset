# ABC069D - Grid Coloring (ARC080D)
from collections.abc import Iterable


def flatten(A: "Array") -> "Array":
    if isinstance(A, Iterable):
        return [i for a in A for i in flatten(a)]
    else:
        return [A]


def main():
    """
    move left to right in odd rows and vice versa in even rows
    1 s--->
    2 <----
    3 --->t
    """
    H, W, N, *A = map(int, open(0).read().split())
    grid = flatten([color] * cnt for color, cnt in enumerate(A, 1))
    for i, g in enumerate(zip(*[iter(grid)] * W)):
        if i & 1 == 0:
            print(*g)
        else:
            print(*g[::-1])


if __name__ == "__main__":
    main()