import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    a, b, c = map(int, input().split())

    print("Yes" if (a+b) >= c else "No")
