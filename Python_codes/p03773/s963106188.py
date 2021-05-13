import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    A,B=map(int,input().split())
    print((A+B)%24)


if __name__ == "__main__":
    main()
