from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N = int(_in[0])  # type:int
    a_arr = list(map(int,_in[1].split(' ')))
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    a_arr.sort(reverse=True)
    cnt = sum(a_arr[1:2*N:2])
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
