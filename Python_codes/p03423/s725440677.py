import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())

    print(n // 3)
