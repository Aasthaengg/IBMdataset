from itertools import groupby
n, k = map(int, input().split())
S = input().strip()
L = [len(list(g)) for v, g in groupby(S)]
if S[0] == '0':
    L = [0] + L
if S[-1] == '0':
    L = L + [0]

A = [sum(L[:2*k+1])]
for i in range(0, len(L)-2*k-1, 2):
    A += A[-1]-L[i]-L[i+1]+L[i+2*k+1]+L[i+2*k+2],
print(max(A))