N = int(input())

DIVIDER = 1000000007

memo = [{} for _ in range(N + 1)]

tab_pow4 = [1]
tab_tmp = 1
for i in range(N):
    tab_tmp *= 4
    tab_pow4.append(tab_tmp)

def dp(Nlen, end):
    if Nlen < len(end):
        return 0
    elif memo[Nlen].setdefault(end, None) != None:
        return memo[Nlen][end]
    #
    if end in ('AGC', 'GAC', 'ACG'):
        ret = 0
    elif Nlen == len(end):
        ret = 1
    else:
        ret = 0
        if end not in ('AGC', 'TGC', 'CGC', 'GGC', 'GAC', 'GTC', 'GCC', 'GGC'):
            ret = (ret + dp(Nlen - 1, 'A' + end[:2])) % DIVIDER
        ret = (ret + dp(Nlen - 1, 'C' + end[:2])) % DIVIDER
        ret = (ret + dp(Nlen - 1, 'G' + end[:2])) % DIVIDER
        ret = (ret + dp(Nlen - 1, 'T' + end[:2])) % DIVIDER
    #
    memo[Nlen][end] = ret
    return ret

import itertools

ans = 0
for end in itertools.product('ACGT', repeat=3):
    if end in ('AGC', 'CAG', 'ACG'): continue
    ans = (ans + dp(N, ''.join(end))) % DIVIDER

# for i in range(N + 1):
#     print("#", memo[i], sum(memo[i].values()))
print(ans)