def slove():
    import sys
    import collections
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    a = str(input().rstrip('\n'))
    b = str(input().rstrip('\n'))
    c = str(input().rstrip('\n'))
    cnt = 0
    for i in range(n):
        s = collections.Counter([a[i], b[i], c[i]])
        if len(s) == 3:
            cnt += 2
        elif len(s) == 2:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    slove()
