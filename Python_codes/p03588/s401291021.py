def slove():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    ab = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
    ab.sort()
    print(ab[-1][0] + ab[-1][1])


if __name__ == '__main__':
    slove()
