def slove():
    import sys
    input = sys.stdin.readline
    a, b, c = list(map(int, input().rstrip('\n').split()))
    print("YES" if b - a == c - b else "NO")


if __name__ == '__main__':
    slove()
