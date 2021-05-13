import sys
input = sys.stdin.readline

N, K = [int(item) for item in input().split()]
A = [int(item) for item in input().split()]


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors


d_cand = make_divisors(sum(A))
d_cand.sort()
d_cand.reverse()

for d in d_cand:
    r = [a % d for a in A]
    rp_sum = sum(r)
    rm_sum = 0
    if rp_sum % d != 0:
        continue
    r.sort()

    for i in range(N):
        # index i まで r-, i+1から r+
        rp_sum -= r[i]
        rm_sum += r[i]

        n_min = max(0, -(rm_sum + rp_sum) / d + (N - i - 1))
        n_max = (K - rm_sum) / d
        if n_min <= n_max and (n_min % 1 == 0 or n_max % 1 == 0 or int(n_min) != int(n_max)):
            print(d)
            break
    else:
        continue
    break
