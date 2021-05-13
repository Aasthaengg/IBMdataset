# coding: utf-8
import sys
from functools import lru_cache

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
N = ir()

def ok(last4):
    if last4.find('AGC') != -1:
        return False
    for i in range(3):
        s = list(last4)
        s[i], s[i+1] = s[i+1], s[i]
        if ''.join(s).find('AGC') != -1:
            return False
    return True

@lru_cache(None)
def dfs(i, last3):
    if i == N:
        return 1
    ret = 0
    for la in 'AGCT':
        if ok(last3+la):
            ret += dfs(i+1, last3[1:]+la)
    return ret % MOD

answer = dfs(0, 'TTT')
print(answer % MOD)
