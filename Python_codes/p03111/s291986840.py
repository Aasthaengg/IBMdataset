from sys import stdin
from itertools import product


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N,A,B,C = list(map(int,_in[0].split(' ')))  # type:list(int)
    l_arr = []
    for i in range(N):
        _ = int(_in[i+1])  # type:int
        l_arr.append(_)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    cnt = float('inf')
    cand_arr = list(product([0,1,2,3],repeat=N))
    for cand in cand_arr:
        length = [0,0,0,0]
        if (1 in cand) and (2 in cand) and (3 in cand):
            for i,_len in zip(cand,l_arr):
                length[i] += _len
            _cnt = abs(A-length[1])+abs(B-length[2])+abs(C-length[3])+\
                   10*(N-cand.count(0)-3)
            cnt = min(cnt,_cnt)
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
