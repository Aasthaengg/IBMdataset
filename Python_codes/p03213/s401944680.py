from functools import reduce


def solve(N):
    if N <= 1:
        return 0
    primes = [
        2, 3, 5, 7, 11,
        13, 17, 19, 23, 29,
        31, 37, 41, 43, 47,
        53, 59, 61, 67, 71,
        73, 79, 83, 89, 97,
    ]
    primes = [p for p in primes if p <= N]
    exps = [0] * len(primes)
    for i in range(len(primes)):
        p = primes[i]
        pi = p
        while pi <= N:
            exps[i] += N // pi
            pi *= p

    ans = 0
    for i in range(len(exps)):
        a = exps[i]

        if 74 <= a:  # 75
            ans += 1

        for j in range(i + 1, len(exps)):
            b = exps[j]

            if 24 <= a and 2 <= b:  # 25*3
                ans += 1
            if 24 <= b:  # 3*25
                ans += 1

            if 14 <= a and 4 <= b:  # 15*5
                ans += 1
            if 14 <= b:  # 5*15
                ans += 1

            for k in range(j + 1, len(exps)):
                c = exps[k]

                if 4 <= c:  # 3*5*5 or 5*3*3
                    ans += 2
                if 4 <= b and 2 <= c:  # 5*5*3
                    ans += 1

    return ans


N = int(input())
print(solve(N))