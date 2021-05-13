def f(n):
    cnt = 0
    while n % 2 == 0:
        n //= 2
        cnt += 1
    return cnt


def main():
    N = int(input())
    a = list(map(int, input().split(' ')))
    exp_2 = list(map(f, a))
    print(sum(exp_2))


if __name__ == '__main__':
    main()
