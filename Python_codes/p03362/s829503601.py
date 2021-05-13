import sys

input = sys.stdin.readline


def calc_prime_numbers(n):
    """Sieve of Eratosthenes"""
    if n == 1:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False

    prime_number_list = []
    for i in range(n + 1):
        if is_prime[i]:
            prime_number_list.append(i)

    return prime_number_list


def main():
    N = int(input())

    MAX_A = 55555
    prime_numbers = calc_prime_numbers(MAX_A)

    ans = []
    for prime_number in prime_numbers:
        if prime_number % 5 == 1:
            ans.append(prime_number)

        if len(ans) == N:
            break

    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
