import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    S = input()
    if int(S[:4]) < 2018:
        print("Heisei")
    elif int(S[:4]) > 2019:
        print("TBD")
    else:
        if int(S[5:7]) > 4:
            print("TBD")
        else:
            print("Heisei")

if __name__ == "__main__":
    main()
