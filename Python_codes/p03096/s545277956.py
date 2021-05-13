from collections import Counter, defaultdict


def main():
    # n,m = [int(z) for z in input().split()]
    # table =[
    #     [int(z) for z in input().split()]
    #     for _ in range(n)
    # ]
    V = 10 ** 9 + 7
    n = int(input())
    c = [int(input()) for _ in range(n)]

    table = [0] * (n + 1)
    table[0] = 1

    D = defaultdict(lambda: 0)

    for i in range(n):
        ci = c[i]
        if i != 0:
            if c[i - 1] == ci:
                table[i + 1] = table[i] % V
                continue

        res = table[i]
        pre = D[ci]
        res += pre
        table[i + 1] = res % V

        D[ci] = D[ci] + table[i] % V

    print(table[-1])


if __name__ == '__main__':
    main()
