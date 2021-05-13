import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    def make_divisors(n):
        divisors = []
        for i in range(1, int(pow(n, 0.5)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        divisors.sort()
        return divisors

    max_num = m // n
    divisors = make_divisors(m)
    res = 1
    for div in divisors:
        if div <= max_num:
            res = div
        else:
            break

    print(res)




if __name__ == '__main__':
    resolve()
