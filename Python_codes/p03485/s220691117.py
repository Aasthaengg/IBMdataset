from sys import stdin
import math


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    a,b = list(map(int,_in[0].split(' ')))  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    cnt = math.ceil((a+b)/2)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
