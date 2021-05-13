from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N, K = list(map(int,_in[0].split(' ')))
    l_arr = list(map(int,_in[1].split(' ')))
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    l_arr.sort(reverse=True)
    cnt = sum(l_arr[:K])
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
