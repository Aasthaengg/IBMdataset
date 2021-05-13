mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    for a in A:
        cnt += a&1
    if cnt&1:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()
