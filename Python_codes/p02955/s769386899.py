import itertools
import bisect
N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort(reverse=True)
    return divisors


divisors = make_divisors(sum(A))
for d in divisors:
    b = []
    for a in A:
        b += [a % d]
    b.sort()
    c = [0] + list(itertools.accumulate(b))
    il = bisect.bisect_left(c, K)
    if il >= len(c) or d * (len(c) - il - 1) - (c[-1] - c[il]) <= K:
        print(d)
        exit()
