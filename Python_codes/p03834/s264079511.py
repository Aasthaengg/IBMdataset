import sys
def input(): return sys.stdin.readline().strip()


def main():
    s = input().split(",")
    print("{} {} {}".format(s[0], s[1], s[2]))

if __name__ == "__main__":
    main()
