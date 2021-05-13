import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def create_integer_string(counts):
    res = ""

    for i in range(9, 0, -1):
        count = counts[i]
        res += str(i) * count

    return res


def main():
    from copy import copy

    n, m = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    a.sort()
    pat = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    match_nums = dict()

    for x in a:
        match_num = pat[x]
        match_nums[match_num] = x

    dp = [0] * (n + 1)
    dp_c = [[0] * 10 for _ in range(n + 1)]

    for i in range(n + 1):
        for match_num, val in match_nums.items():
            if i + match_num > n:
                continue
            if i > 0 and dp[i] == 0:
                continue
            if dp[i + match_num] < dp[i] + 1:
                dp[i + match_num] = dp[i] + 1
                dp_c[i + match_num] = copy(dp_c[i])
                dp_c[i + match_num][val] += 1
            elif dp[i + match_num] == dp[i] + 1:
                counts_cur = copy(dp_c[i + match_num])
                cur = create_integer_string(counts_cur)
                counts_new = copy(dp_c[i])
                counts_new[val] += 1
                new = create_integer_string(counts_new)
                if new > cur:
                    dp[i + match_num] = dp[i] + 1
                    dp_c[i + match_num] = copy(dp_c[i])
                    dp_c[i + match_num][val] += 1

    counts = dp_c[n]

    print(create_integer_string(counts))


if __name__ == '__main__':
    main()
