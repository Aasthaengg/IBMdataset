import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    m = int(input())

    print(24 - m + 24)
