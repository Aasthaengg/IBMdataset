# coding: utf-8
N = int(input())

arrays = list("abcdefghij")
pat_dic = {i:arrays[i] for i in range(N)}
par_patterns = list(range(10))

patterns = par_patterns[:N]
def next_search(arr,N):
    tmp = arr.copy()
    if len(tmp) == N:
        print(''.join([pat_dic[tmp[i]] for i in range(N)]))
        return None
    for st in patterns:
        if max([0]+tmp)+1 < st:
            continue
        tmp.append(st)
        if tmp[0] != 0:
            continue

        next_search(tmp, N)
        tmp = arr.copy()

next_search([], N)