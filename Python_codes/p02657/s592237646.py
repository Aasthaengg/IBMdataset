import math  # noqa: F401
from typing import Dict, List, Optional, Tuple, Union  # noqa: F401


def main(A: int, B: int):
    print(A * B)


if __name__ == "__main__":
    A, B = map(int, input().split())
    main(A, B)
