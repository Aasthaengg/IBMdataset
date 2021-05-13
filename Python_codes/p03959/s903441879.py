import sys
mod = 10**9 + 7

def nai():
    print(0)
    sys.exit()

N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

M = max(A)
if M != max(T):
    nai()

iT = T.index(M)
iA = N - 1 - A[::-1].index(M)
if iA < iT:
    nai()
ans = pow(M, max(0, iA - iT - 1), mod)
pre = -1
for t in T[:iT]:
    if pre == t:
        ans = t*ans%mod
    pre = t
pre = -1
for a in A[::-1]:
    if a == M:
        break
    if pre == a:
        ans = a*ans%mod
    pre = a
print(ans)