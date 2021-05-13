def restore():
    for i in range(N - M, -1, -1):
        if all(s == '?' or s == t for s, t in zip(S[i:i + M], T)):
            ans = S[:i] + T + S[i + M:]
            return ''.join('a' if c == '?' else c for c in ans)
    return 'UNRESTORABLE'


S = input()
T = input()
N = len(S)
M = len(T)
print(restore())