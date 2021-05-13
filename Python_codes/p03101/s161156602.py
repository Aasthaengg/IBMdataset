import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    H, W = list(map(int, sys.stdin.readline().split()))
    h, w = list(map(int, sys.stdin.readline().split()))
    print(H*W-(h*W)-(w*H)+h*w)



if __name__ == '__main__':
    main()
