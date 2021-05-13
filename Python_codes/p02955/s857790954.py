n, k = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors

G = make_divisors(s)

from itertools import accumulate

for g in G:
    B = [a%g for a in A]
    B.sort()
    B = [0] + B
    B = list(accumulate(B))
    p = 0
    q = 0
    for i in range(n-1):
        p = B[i+1]
        q = g*(n-1-i)-(B[-1]-B[i+1])
        if max(p, q) <= k and (p-q)%g == 0:
            break
    else:
        continue
    break
print(g)