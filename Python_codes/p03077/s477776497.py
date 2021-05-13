import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    time =0

    m =min(A,B,C,D,E)
    time +=math.ceil(N/m) +4
    print(time)







if __name__ == "__main__":
    main()
