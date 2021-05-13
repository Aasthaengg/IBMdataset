def main():
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    N = int(input())
    for h in range(1, 3501):
        if N >= 4 * h:
            continue
        for n in range(h, 3501):
            if N * (h + n) >= 4 * h * n:
                continue
            t1 = N * h * n
            t2 = 4 * h * n - N * n - N * h
            if t1 % t2 == 0:
                print(h, n, t1 // t2)
                return True

if __name__ == '__main__':
    main()