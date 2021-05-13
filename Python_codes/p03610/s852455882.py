import sys
def input(): return sys.stdin.readline().strip()


def main():
    s = input()
    print(s[::2])

if __name__ == "__main__":
    main()
