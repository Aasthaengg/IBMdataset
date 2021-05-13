import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a = int(input())
    if a >=3200:
        print(input())
    else:
        print("red")

if __name__ == "__main__":
    main()
