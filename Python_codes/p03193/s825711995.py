def slove():
    import sys
    input = sys.stdin.readline
    n, h, w = list(map(int, input().rstrip('\n').split()))
    cnt = 0
    for i in range(n):
        a, b = list(map(int, input().rstrip('\n').split()))
        cnt += min(a // h, b // w)
    print(cnt)


if __name__ == '__main__':
    slove()
