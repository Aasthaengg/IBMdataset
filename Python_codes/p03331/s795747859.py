import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())

    ans = float("inf")

    for a in range(1, N):
        b = N - a
        tmp = 0
        for s in str(a):
            tmp += int(s)
        for s in str(b):
            tmp += int(s)

        ans = min(ans, tmp)

    print(ans)



if __name__ == '__main__':
    main()

