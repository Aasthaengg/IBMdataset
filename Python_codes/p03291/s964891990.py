import functools
import os
import sys

sys.setrecursionlimit(10000)
INF = float('inf')


def debug(fn):
    if not os.getenv('LOCAL'):
        return fn

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        print('DEBUG: {}({}) -> '.format(
            fn.__name__,
            ', '.join(
                list(map(str, args)) +
                ['{}={}'.format(k, str(v)) for k, v in kwargs.items()]
            )
        ), end='')
        print(ret)
        return ret

    return wrapper


# @debug
# @functools.lru_cache(maxsize=None)
# def solve(idx, abc=3):
#     """
#     S[0:idx+1] の ABC 数の数
#     abc=2 なら AB 数、abc=1 なら A 数、abc=0 なら今までのパターン数
#     :param idx:
#     :param abc:
#     :return:
#     """
#     if idx < 0:
#         return 1 if abc == 0 else 0
#     c = S[idx]
#     if 1 <= abc <= 3:
#         if c == '0ABC'[abc]:
#             return (solve(idx - 1, abc=abc) + solve(idx - 1, abc=abc - 1)) % MOD
#         elif c == '?':
#             return (solve(idx - 1, abc=abc) * 3 + solve(idx - 1, abc=abc - 1)) % MOD
#         else:
#             return (solve(idx - 1, abc=abc)) % MOD
#     elif abc == 0:
#         if c == '?':
#             return (solve(idx - 1, abc=0) * 3) % MOD
#         else:
#             return (solve(idx - 1, abc=0)) % MOD


S = input()
MOD = 10 ** 9 + 7
# print(solve(len(S) - 1) % MOD)

# ↑の DP 版
# dp[i][3]: S[0:i] の ABC 数
# dp[i][2]: S[0:i] の AB 数
# dp[i][1]: S[0:i] の A 数
# dp[i][0]: S[0:i] の組み合わせ数
# dp = np.empty((len(S) + 1, 4))
# dp[0][0] = 1
# for i in range(len(S)):
#     c = S[i]
#     if c == '?':
#         dp[i + 1][0] = dp[i][0] * 3 % MOD
#     else:
#         dp[i + 1][0] = dp[i][0] % MOD
#     for abc in [1, 2, 3]:
#         if c == '0ABC'[abc]:
#             dp[i + 1][abc] = (dp[i][abc] + dp[i][abc - 1]) % MOD
#         elif c == '?':
#             dp[i + 1][abc] = (dp[i][abc] * 3 + dp[i][abc - 1]) % MOD
#         else:
#             dp[i + 1][abc] = dp[i][abc] % MOD
#     # dp[i + 1, :] %= MOD
# print(int(dp[len(S), 3]))


# ↑の配列再利用版
dp = [0] * 4
dp[0] = 1
for i in range(len(S)):
    c = S[i]
    for abc in [3, 2, 1]:
        if c == '0ABC'[abc]:
            dp[abc] = (dp[abc] + dp[abc - 1]) % MOD
        elif c == '?':
            dp[abc] = (dp[abc] * 3 + dp[abc - 1]) % MOD
    if c == '?':
        dp[0] = dp[0] * 3 % MOD
print(int(dp[3]))
