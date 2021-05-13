def slove():
    import sys
    input = sys.stdin.readline
    a, b, c = list(map(str, str(input().rstrip('\n')).split()))
    print("YES" if a[-1] == b[0] and b[-1] == c[0] else "NO")


if __name__ == '__main__':
    slove()
