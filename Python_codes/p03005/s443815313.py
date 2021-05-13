def slove():
    import sys
    input = sys.stdin.readline
    n, k = list(map(int, input().rstrip('\n').split()))
    ls = [0] * k
    pos = 0
    for i in range(n):
        ls[pos] += 1
        if pos + 1 < k:
            pos += 1
    print(0 if len(ls) == 1 else ls[-1] - ls[0])


if __name__ == '__main__':
    slove()
