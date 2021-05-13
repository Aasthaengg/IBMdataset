import sys
input = sys.stdin.readline


def readstr():
    return input().strip()


def readint():
    return int(input())


def readnums():
    return map(int, input().split())


def readstrs():
    return input().split()


def main():
    N, K = readnums()
    x = list(readnums())
    ans = 0
    for i in range(K - 1, N):
        ls = i - K + 1
        le = i
        if x[ls] > 0:
            val = abs(x[le])
        elif x[le] < 0:
            val = abs(x[ls])
        else:
            val = abs(x[ls]) + abs(x[le])
            val += min(abs(x[ls]), abs(x[le]))
        if not ans:
            ans = val
        else:
            ans = min(ans, val)

    print(ans)


if __name__ == "__main__":
    main()
