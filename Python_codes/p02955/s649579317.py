def divisors(N):
    U = int(N ** 0.5) + 1
    L = [i for i in range(1, U) if N % i == 0]
    return L + [N // i for i in reversed(L) if N != i * i]

N, K = map(int,input().split())
A = list(map(int,input().split()))
for d in reversed(divisors(sum(A))):
    R = sorted(a % d for a in A)
    # print(d,R,-sum(R) // d,sum(R[:-sum(R) // d]))
    if sum(R[:-sum(R) // d]) <= K:
        print(d)
        quit()

