import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    d =(N-1)//111
    print((d+1)*111)


if __name__ == "__main__":
    main()
