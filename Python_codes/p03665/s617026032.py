from math import factorial

def com(n, r):
    return fac_n // factorial(r) // factorial(n - r)


N, P = map(int, input().split())
A = [int(x) for x in input().split()]

odd, even = 0, 0
for i in range(N):
    if A[i] % 2 == 1:
        odd += 1
    else:
        even += 1

fac_n = factorial(odd)

res = 0
for r in range(P, odd+1, 2):
    res += com(odd, r)
ans = res * (2**even)

print(ans)