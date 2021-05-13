from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N = int(_in[0])  # type:int
    A_arr = list(map(int,_in[1].split(' ')))  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    cnt = 0
    i = -1
    while True:
        i += 1
        while i<N-1 and A_arr[i]==A_arr[i+1]:
            i += 1
        if i<N-1 and A_arr[i]<=A_arr[i+1]:
            while i<N-1 and A_arr[i]<=A_arr[i+1]:
                i += 1
        elif i<N-1 and A_arr[i]>=A_arr[i+1]:
            while i<N-1 and A_arr[i]>=A_arr[i+1]:
                i += 1
        cnt += 1
        if i>=N-1:
            break
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
