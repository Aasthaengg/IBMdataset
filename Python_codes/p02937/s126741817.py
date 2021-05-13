import sys
S = list(input())
T = list(input())
C = {}
for i in range(97, 97+26):
    C[chr(i)] = -1

k = len(T)
for i in range(len(S)):
    if C[S[i]] == -1:
        C[S[i]] = [i]
    else:
        C[S[i]].append(i)

p = 0
now = -1
ans = 0
used = {}
L = {}
for i in range(97, 97+26):
    used[chr(i)] = 0
    if C[chr(i)] == -1:
        L[chr(i)] = 0
    else:
        L[chr(i)] = len(C[chr(i)])

while(True):
    n = T[p]
    if C[n] == -1:
        print(-1)
        sys.exit()
    else:
        if used[n] >= L[n]:
            p -= 1
            for i in range(97, 97 + 26):
                used[chr(i)] = 0
            ans += len(S) - now - 1
            now = -1
        elif C[n][used[n]] >= now:
            ans += C[n][used[n]] - now
            now = C[n][used[n]]
            used[n] += 1
        else:
            used[n] += 1
            p -= 1
    p += 1
    if p == k:
        print(ans)
        break