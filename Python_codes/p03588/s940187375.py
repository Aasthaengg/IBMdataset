mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    AB = []
    for _ in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))
    AB.sort(key=lambda x: x[0])
    print(AB[-1][0] + AB[-1][1])


if __name__ == '__main__':
    main()
