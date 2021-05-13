S = input()
N = len(S)

MOD = 10 ** 9 + 7

def nLeftA(S, A):
    """(S[:i]の'A'の選び方, S[:i]の'?'の埋め方)"""
    l = [(0, 1)]
    for s in S:
        a, q = l[-1]
        if s == A:
            a = q + a      # S[i-1]を選ぶ + S[:i]のどれかを選ぶ
        elif s == '?':
            a = q + a * 3  # S[i-1]を選ぶ + S[:i]のどれかを選ぶ(?に3通り)
            q = q * 3
        l.append((a % MOD, q % MOD))
    return l

l = nLeftA(S, 'A')
r = nLeftA(reversed(S), 'C')
r.reverse()
r = r[1:]

n = 0
for i in range(N):
    if S[i] in 'B?':
        n += l[i][0] * r[i][0] % MOD

print(n % MOD)
