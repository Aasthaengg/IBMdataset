n = int(input())

mod = 10 ** 9 + 7

if n == 3:
    print(61)
else:

    from collections import defaultdict
    from itertools import product
    keys = []
    for prod in product('AGCT', 'AGCT', 'AGCT', 'AGCT'):
        last = ''.join(prod)
        f = ('AGC' not in last)

        for i in range(len(last) - 1):
            last2 = list(last)
            last2[i], last2[i+1] = last2[i+1], last2[i]
            last2 = ''.join(last2)
            if 'AGC' in last2:
                f = False

        if f:
            keys.append(''.join(last))

    dp = dict()
    for key in keys:
        dp[key] = 1

    for _ in range(4, n):
        dp_new = defaultdict(int)

        for key in keys:
            for char in 'AGCT':
                last = (key + char)[1:]
                f = ('AGC' not in last)

                for i in range(len(last) - 1):
                    last2 = list(last)
                    last2[i], last2[i+1] = last2[i+1], last2[i]
                    last2 = ''.join(last2)
                    if 'AGC' in last2:
                        f = False

                if f:
                    dp_new[''.join(last)] += dp[key]

        dp = dict()
        for key in keys:
            dp[key] = dp_new[key] % mod

    print(sum(list(dp.values())) % mod)
