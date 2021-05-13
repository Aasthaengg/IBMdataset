from collections import Counter

MOD = 10 ** 9 + 7

def factorize(n):
    """ Simple factorize
    :param n: number to factorize
    :return: list of factors
       time complexity : O(n√n)
       space complexity : O(n)
    """
    factors = []
    for i in range(2, n+1):
        while n % i == 0:
            n = n // i
            factors.append(i)
    return factors

def main():
    N = int(input())

    factors = []
    for i in range(1, N+1):
        factors += factorize(i)
    factor_counts = list(Counter(factors).values())

    ans = 1
    for v in factor_counts:
        ans = ans * (v+1) % MOD

    print(ans)

main()