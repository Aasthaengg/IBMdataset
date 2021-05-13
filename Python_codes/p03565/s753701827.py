import sys
S = list(input())
T = list(input())
s = len(S)
t = len(T)
if s < t:
    print('UNRESTORABLE')
    sys.exit()
OK = False
P = 0
for i in range(s - t + 1):
    if S[i] != T[0] and S[i] != '?':
        continue
    for j in range(1, t + 1):
        if j == t:
            OK = True
            P = i
            break
        if S[i + j] != T[j] and S[i + j] != '?':
            break
for k in range(t):
    S[P + k] = T[k]
for i in range(s):
    if S[i] == '?':
        S[i] = 'a'
if OK:
    [print(S[i], end='') for i in range(s)]
    print('')
else:
    print('UNRESTORABLE')