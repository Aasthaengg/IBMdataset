import sys
def input(): return sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    if n == 1 and m == 1: ans = 1
    elif m == 1: ans = n - 2
    elif n == 1: ans = m - 2
    else: ans = (m - 2) * (n - 2)
    print(ans)


if __name__ == "__main__":
    main()
