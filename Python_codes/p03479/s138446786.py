import sys
def input(): return sys.stdin.readline().strip()


def main():
    x, y = map(int, input().split())
    cnt = 0
    while x <= y:
        x *= 2
        cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
