N, K = [int(zz) for zz in input().split()]
A = [int(zz) for zz in input().split()]

A.sort(reverse=True)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

P = make_divisors(sum(A))
P.sort(reverse=True)

for p in P:
    z = 0
    for i in range(N):
        z += A[i] % p
    if z % p == 0:
        B = [i % p for i in A]
        B.sort(reverse=True)
        q = z//p
        j = 0
        for i in range(q):
            j += p-B[i]
        if K >= j:
            print(p)
            exit()
            
print(p)
