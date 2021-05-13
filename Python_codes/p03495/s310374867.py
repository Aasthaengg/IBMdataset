from sys import stdin
from collections import Counter


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N, K = list(map(int,_in[0].split(' ')))  # type:list(int)
    A_arr = list(map(int,_in[1].split(' ')))  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    counter = Counter(A_arr)
    counter = list(counter.values())
    counter.sort(reverse=True)
    cnt = sum(counter[K:])
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
