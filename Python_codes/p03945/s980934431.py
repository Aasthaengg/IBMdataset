def run_length_encoding(s):
    '''連長圧縮を行う
    s ... iterable object e.g. list, str
    return
    ----------
    s_composed,s_num,s_idx
    それぞれ、圧縮後の文字列、その文字数、その文字が始まるidx'''
    from itertools import groupby
    s_composed, s_sum = [], []
    s_idx = [0]
    for k, v in groupby(s):
        s_composed.append(k)
        n = len(list(v))
        s_sum.append(n)
        s_idx.append(s_idx[-1] + n)

    # assert len(s_sum) == len(s_composed)
    return s_composed, s_sum, s_idx


S_composed, _, _ = run_length_encoding(input())
print(len(S_composed) - 1)
