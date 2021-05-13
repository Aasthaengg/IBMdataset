from sys import stdin
import math


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N = int(_in[0])  # type:int
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    cnt = math.factorial(N)%(10**9+7)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
