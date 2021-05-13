import sys

def input():
    return sys.stdin.readline().strip()

def main():
    a, b, t = map(int, input().split())
    count = t // a
    print(b*count)


main()