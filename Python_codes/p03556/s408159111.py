import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    ans = 1
    while ans ** 2 <= n: ans += 1
    print((ans - 1) ** 2)

if __name__ == "__main__":
    main()
