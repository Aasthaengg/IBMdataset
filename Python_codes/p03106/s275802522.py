def abc120_b():
    a, b, k = map(int, input().split(' '))
    n = min(a, b)
    divisors = []

    for i in range(1, n + 1):
        if (a % i == 0) and (b % i == 0):
            divisors.append(i)
    print(divisors[-1 * k])

if __name__ == '__main__':
    abc120_b()