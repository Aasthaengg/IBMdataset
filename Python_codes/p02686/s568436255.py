import sys
input = sys.stdin.readline

N = int(input())
S = [input().rstrip() for _ in range(N)]

A = []
B = []

for s in S:
    a = 0
    k = 0
    for i in range(len(s)):
        if s[i] == ')':
            k += 1
        else:
            k -= 1
        a = max(a, k)
    b = 0
    k = 0
    for i in range(len(s))[::-1]:
        if s[i] == '(':
            k += 1
        else:
            k -= 1
        b = max(b, k)
    A.append(a)
    B.append(b)

L = []
R = []

for i in range(N):
    if B[i] - A[i] >= 0:
        L.append((A[i], i))
    else:
        R.append((B[i], i))

L.sort()
R.sort(reverse=True)

T = []

for a, i in L:
    T.append(S[i])

for b, i in R:
    T.append(S[i])

T = ''.join(T)

k = 0

for t in T:
    if t == '(':
        k += 1
    else:
        k -= 1
    if k < 0:
        print('No')
        break
else:
    if k == 0:
        print('Yes')
    else:
        print('No')