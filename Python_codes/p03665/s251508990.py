import collections, math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N, P = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] = A[i] % 2
c = collections.Counter(A)
zero = c[0]
one = c[1]

ans = 0
if P == 0:
    for i in range(0, one + 1, 2):
        ans += (2 ** zero) * (combinations_count(one, i) )
else:
    for i in range(1, one + 1, 2):
        ans += (2 ** zero) * (combinations_count(one, i) )
print(ans)