N = int(input())

memo = [{} for _ in range(N)]  # i 文字目に dict.key がきたとき, これ以降を何通りあるか を保存する


def judge(last):
    if last[1:] in ('AGC', 'ACG', 'GAC'):
        return False
    if last[0] == 'A':
        if last[1] == 'G' and last[-1] == 'C': return False
        if last[2] == 'G' and last[-1] == 'C': return False
    return True


MOD = 10 ** 9 + 7


def dfs(i, last):
    if i >= N:  # 末尾
        return 1

    if last in memo[i]:
        return memo[i][last]

    res = 0
    for c in 'AGCT':
        l = last[1:] + c
        if judge(l):
            res += dfs(i + 1, l) % MOD
    memo[i][last] = res % MOD
    return res


print(dfs(0, 'XXXX') % MOD)
