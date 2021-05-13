def main():
    n, m = input().split(' ')
    print(mul(n, m))


def mul(n: str, m: str) -> int:
    n = int(n)
    m = int(f'{m[:-3]}{m[-2:]}')

    return (n * m) // 100


if __name__ == '__main__':
    main()
