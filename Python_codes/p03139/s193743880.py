import sys

def r(n, a, b):
    both_max = min(a, b)
    if 0 < a + b - n:
        both_min = a + b - n
    else:
        both_min = 0

    print(both_max, both_min)


def main():
    input = sys.stdin.readline
    n, a, b = list(map(int, input().split()))
    r(n, a, b)


if __name__ == '__main__':
    main()
