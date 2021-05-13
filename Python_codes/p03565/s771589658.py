S = list(input())
T = list(input())
s = len(S)
t = len(T)
X = False
k = -1
for i in range(s - t + 1):
    OK = True
    for j in range(t):
        if S[i + j] != '?' and S[i + j] != T[j]:
            OK = False
            break
    if OK:
        k = i
if k != -1:
    for j in range(t):
        S[k + j] = T[j]
    X = True
if not X:
    print('UNRESTORABLE')
else:
    for i in range(s):
        if S[i] == '?':
            S[i] = 'a'
        print(S[i], end='')
    print('')