N, K = map(int, input().split())
A = list(map(int, input().split()))

P = "POSSIBLE"
IP = "IMPOSSIBLE"

M = max(A)

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)

t = gcd(A[0], A[0])
if N > 1:
    for a in A[1:]:
        t = gcd(t, a)

if K%t == 0 and K <= M:
    print(P)
else:
    print(IP)