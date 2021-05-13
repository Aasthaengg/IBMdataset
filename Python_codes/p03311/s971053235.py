def slove():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    a = list(map(int, input().rstrip('\n').split()))
    b = []
    for i, v in enumerate(a):
        b.append(v - (i + 1))
    b.sort()
    t = b[len(b) // 2]
    s = 0
    for i, v in enumerate(a):
        s += abs(v - (t + (i + 1)))
    print(s)


if __name__ == '__main__':
    slove()
