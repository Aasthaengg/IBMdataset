def slove():
    import sys
    input = sys.stdin.readline
    x, a, b = list(map(int, input().rstrip('\n').split()))
    if abs(x - a) < abs(x - b):
        print("A")
    elif abs(x - a) > abs(x - b):
        print("B")


if __name__ == '__main__':
    slove()
