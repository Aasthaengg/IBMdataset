
def func(rl_str):
    r_n = rl_str.count('R')
    l_n = rl_str.count('L')
    res = []
    for _ in range(r_n - 1):
        res.append(0)
    res.append((r_n-1)//2 + 1 + l_n//2)
    res.append(r_n//2 + (l_n-1)//2 + 1)
    for _ in range(l_n - 1):
        res.append(0)
    return res

if __name__ == '__main__':
    S = input()
    lst = []
    n_st = 0
    str_lst = []
    for n_en, (i_1, i_2) in enumerate(zip(S[:-1], S[1:])):
        n_en += 1
        if i_1 == 'L' and i_2 == 'R':
            lst.append(n_en)
            str_lst.append(S[n_st:n_en])
            n_st = n_en
    str_lst.append(S[n_st:])

    result = []
    for _str in str_lst:
        res_tmp = func(_str)
        result += res_tmp
    print(*result)
