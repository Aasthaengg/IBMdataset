def resolve():
    '''
    code here
    '''
    import collections
    import itertools
    import numpy as np
    N = int(input())
    Ss = [input()[0] for _ in range(N)]

    march_letter = [item for item in Ss if item in ['M', 'A', 'R', 'C', 'H']]
    march_cnt = collections.Counter(march_letter)

    if len(march_cnt) < 3:
        res = 0
    else:
        res_list = itertools.combinations(march_cnt.values(),3)

        res = 0
        for element in res_list:
            res += np.prod(np.array(element))
    print(res)

if __name__ == "__main__":
    resolve()
