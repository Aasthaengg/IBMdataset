N = int(input())
MOD = 10 ** 9 + 7

memo = [{} for _ in range(N)]

def ok(last4):
    if last4.find('AGC') != -1:
        return False
    for i in range(3):
        t = list(last4)
        t[i], t[i+1] = t[i+1], t[i]
        if ''.join(t).find('AGC') != -1:
            return False
    return True

def dfs(i, last3):
    if i == N:
        return 1
    if last3 in memo[i]:
        return memo[i][last3]
    ret = 0
    for s in 'ACGT':
        if ok(last3+s):
            ret = (ret + dfs(i+1, last3[1:]+s)) % MOD
    memo[i][last3] = ret
    return ret

answer = dfs(0, 'TTT')
print(answer)
