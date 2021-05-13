import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    R = int(sys.stdin.readline().rstrip())
    G = int(sys.stdin.readline().rstrip())
    print(2*G-R)



if __name__ == '__main__':
    main()
