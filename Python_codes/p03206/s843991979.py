import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    D = int(sys.stdin.readline().rstrip())
    print('Christmas' + ' Eve'*(25-D))



if __name__ == '__main__':
    main()
