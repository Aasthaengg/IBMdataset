from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N,C,K = list(map(int,_in[0].split(' ')))  # type:list(int)
    T_arr = []
    for i in range(N):
        _ = int(_in[i+1])  # type:int
        T_arr.append(_)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    T_arr.sort()
    cnt = 0
    i = 0
    while True:
        c = 1
        tlim = T_arr[i]+K
        i += 1
        while i<N and T_arr[i]<=tlim and c+1<=C:
            i += 1
            c += 1
        cnt += 1
        if i>=N:
            break
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
