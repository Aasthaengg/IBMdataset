# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
N = ir()
memo = [{} for _ in range(N+1)]

def ok(last4):
    if last4.find('AGC') != -1:
        return False
    for i in range(3):
        s = list(last4)
        s[i], s[i+1] = s[i+1], s[i]
        if ''.join(s).find('AGC') != -1:
            return False
    return True

def dfs(i, last3):
    if i == N:
        return 1
    if last3 in memo[i]:
        return memo[i][last3]
    ret = 0
    for la in 'AGCT':
        if ok(last3+la):
            ret += dfs(i+1, last3[1:]+la)
    ret %= MOD
    memo[i][last3] = ret
    return ret

answer = dfs(0, 'TTT')
print(answer % MOD)
