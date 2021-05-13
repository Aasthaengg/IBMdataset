def slove():
    import sys
    import collections
    input = sys.stdin.readline
    x, y = list(map(int, input().rstrip('\n').split()))
    d = collections.defaultdict(list)
    if x % y == 0:
        print(-1)
    else:
        print(x)


if __name__ == '__main__':
    slove()
