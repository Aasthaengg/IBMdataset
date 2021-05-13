import functools
def primes(n):

    prime_list = list(range(n+1))
    prime_list[1] = 0
    for i in range(2, int(n)+1):
        if prime_list[i] != 0:
            for j in range(2*i, n+1, i):
                prime_list[j] = 0

    return [i for i in prime_list if i != 0]

def solve(n):

    prime_list = primes(n)
    powers = []
    for p in prime_list:
        tmp = 0
        a = p
        while a <= n:
            tmp += n // a
            a *= p
        powers.append(tmp)

    ans = functools.reduce(
        lambda acc, x: (acc*(x+1)) % (10**9+7), powers, 1)

    return ans

if __name__ == "__main__":
    n = int(input())
    print(solve(n))