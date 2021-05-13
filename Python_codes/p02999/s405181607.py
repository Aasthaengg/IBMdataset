def slove():
    import sys
    input = sys.stdin.readline
    x, a = list(map(int, input().rstrip('\n').split()))
    print(0 if x < a else 10)


if __name__ == '__main__':
    slove()
