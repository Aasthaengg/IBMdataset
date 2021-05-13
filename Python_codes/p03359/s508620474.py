import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    a, b = map(int, input().split())

    month_diff = a-1
    if a <= b:
        month_diff += 1

    print(month_diff)
