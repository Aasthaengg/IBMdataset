import sys
def input(): return sys.stdin.readline().strip()


def main():
    x = int(input())
    time, rem = x // 11, x % 11
    if 0 < rem <= 6:
        print(time * 2 + 1)
    elif 6 < rem:
        print(time * 2 + 2)
    else:
        print(time * 2)


if __name__ == "__main__":
    main()
