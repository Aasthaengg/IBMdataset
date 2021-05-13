from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    S_arr = _in[0]  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    N = len(S_arr)-1
    cnt = 0
    for bit in range(1<<N):
        # bit = 0: '', 1: '+'
        tmp = []
        pointa = 0
        for i in range(N):
            if bit&(1<<i):
                tmp.append(int(S_arr[pointa:i+1]))
                pointa = i+1
        else:
            tmp.append(int(S_arr[pointa:]))
        cnt += sum(tmp)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
