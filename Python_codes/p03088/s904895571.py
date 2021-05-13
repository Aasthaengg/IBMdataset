mod = 10**9 + 7


n = int(input())

def satisfy(s):
    for i in range(4):
        S = list(s)
        if i >= 1:
            S[i - 1], S[i] = S[i], S[i - 1]
        if "AGC" in "".join(S):
            return False
    return True

def dfs(depth, last4):
    if depth == n:
        if satisfy(last4):
            return 1
        else:
            return 0
    if last4 in MEMO[depth]:
        return MEMO[depth][last4]
    if satisfy(last4):
        ret = 0
        for c in "ACGT":
            ret += dfs(depth + 1, last4[1:] + c)
            ret %= mod
        MEMO[depth][last4] = ret
        return ret
    else:
        return 0

MEMO = [{} for _ in range(n + 1)]
print(dfs(0, "TTTT"))
