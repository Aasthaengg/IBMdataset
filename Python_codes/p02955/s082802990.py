from itertools import accumulate

def divisors(N):
    U = int(N ** 0.5) + 1
    L = [i for i in range(1, U) if N % i == 0]
    return L + [N // i for i in reversed(L) if N != i * i]

N, K, *A = map(int, open(0).read().split())

for d in reversed(divisors(sum(A))):
    R = [0] + list(accumulate(sorted(a % d for a in A)))
    for i in range(N):
        l = R[i]
        r = (N - i) * d - (R[N] - R[i])
        if max(l, r) <= K:
            print(d)
            quit()
