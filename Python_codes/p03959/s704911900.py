def inpl(): return [int(i) for i in input().split()]
mod = 10**9+7
N = int(input())
T = inpl()
A = inpl()
summit =  T[-1]
S = [i == j == summit for i, j in zip(A, T)]
ans, pre = 1, 0
if A[0] != summit:
    ans = 0
if not any(S):
    ans = 0

k = sum([min(i, j) == summit for i, j in zip(A, T)]) 
for i in T:
    if i == summit:
        break
    if i == pre:
        ans = ans*pre %mod
    else:
        pre = i
pre = 0
for i in reversed(A):
    if i == summit:
        break
    if i == pre:
        ans = ans*pre %mod
    else:
        pre = i
print(ans*summit**max(k-2, 0)%mod)