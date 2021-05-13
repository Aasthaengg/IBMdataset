import sys

N, Q = map(int, input().split())
S = input()
s = [0]
for i, c in enumerate(S):
    if i == 0:
        s.append(0)
    elif S[i-1] == 'A' and S[i] == 'C':
        s.append(s[-1] + 1)
    else:
        s.append(s[-1])

#print(s)
for i in range(Q):
    l, r = map(int, input().split())
    print(s[r] - s[l])