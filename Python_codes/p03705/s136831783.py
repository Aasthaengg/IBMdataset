from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N, A, B = list(map(int,_in[0].split(' ')))  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    _min = A*(N-1)+B
    _max = A+B*(N-1)
    cnt = max(_max-_min+1,0)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
