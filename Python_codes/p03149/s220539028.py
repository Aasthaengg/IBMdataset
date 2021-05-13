def slove():
    import sys
    input = sys.stdin.readline
    a = list(map(str, str(input().rstrip('\n')).split()))
    a.sort()
    print("YES" if "".join(a) == "1479" else "NO")


if __name__ == '__main__':
    slove()
