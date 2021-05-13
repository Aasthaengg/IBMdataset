N = int(input())
F = [0 for i in range(N+1)]


def fib(n):
    if n == 0 or n == 1:
        F[n] = 1
        return F[n]

    if F[n]:
        return F[n]

    F[n] = fib(n-2) + fib(n-1)
    return F[n]


def main():
    print(fib(N))


if __name__ == '__main__':
    main()

