S = input()
n = len(S)

import string
def f(x, mn=None):
    for c in string.ascii_lowercase:
        if c in x: continue
        if mn and c <= mn: continue
        return c
    return None

if n < 26:
    print(S + f(S))
    exit()

i = n-2
while i >= 0:
    if S[i] < S[i+1]: break
    i -= 1
else:
    print(-1)
    exit()

t = S[:i]
print(t + f(t, S[i]))