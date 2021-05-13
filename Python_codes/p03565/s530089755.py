S = list(input())
T = list(input())

def compare(s, t):
    if len(s) != len(t): return False
    res = True
    for i in range(len(s)):
        res &= (s[i] == t[i] or s[i] == '?')
    return res

n = len(S)
m = len(T)
pos = -1
for i in range(n):
    if compare(S[i:i+m], T):
        pos = i

if pos == -1:
    print('UNRESTORABLE')
else:
    S[pos:pos+m] = T
    S = ''.join(S)
    S = S.replace('?', 'a')
    print(S)