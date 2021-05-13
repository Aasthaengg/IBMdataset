import sys

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    XYZ = [[int(x) for x in input().split()] for _ in range(N)]

    ans = 0
    for i in range(2 ** 3):
        tmp = []
        for v in XYZ:
            total = 0
            for j, v2 in enumerate(v):
                if i >> j & 1:
                    total += v2
                else:
                    total -= v2
            tmp.append(total)

        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))

    print(ans)


if __name__ == '__main__':
    main()
