import sys
import math

def input():
    return sys.stdin.readline().rstrip()


def main():
    N,D = map(int,input().split())
    print(math.ceil(N/(D*2+1)))


if __name__ == "__main__":
    main()
