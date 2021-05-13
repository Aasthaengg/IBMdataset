def slove():
    import sys
    input = sys.stdin.readline
    a, b = list(map(int, input().rstrip('\n').split()))
    if a % 3 == 0 or b % 3 == 0 or (a + b) % 3 == 0:
        print("Possible")
    else:
        print("Impossible")


if __name__ == '__main__':
    slove()
