import sys
def main():
    input = sys.stdin.readline
    N, A, B = map(int, input().split())
    H = [int(input()) for _ in range(N)]

    under = 0
    r = (max(H) + B - 1) // B
    c = A - B
    while r - under > 1:
        m = (r + under) // 2
        rem = 0
        for hi in H:
            hi -= B*m
            if hi <= 0: continue
            rem += (hi + c - 1) // c
        if rem <= m: r = m
        else: under = m
    print(r)

if __name__ == '__main__':
    main()