import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    x,a,b = (int(sys.stdin.readline().rstrip()) for i in range(3))

    print((x-a)%b)



if __name__ == '__main__':
    main()
