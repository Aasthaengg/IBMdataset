import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    ans = 1
    while ans <= N: ans *= 2
    print(ans // 2)

if __name__ == "__main__":
    main()
