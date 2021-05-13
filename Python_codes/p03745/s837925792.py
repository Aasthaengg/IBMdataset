def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().strip().split()]
    f, p = 0, 0
    ans = 0
    for a in A:
        if f == 1:
            if a > p:
                f = 2
            elif a < p:
                f = 3
        elif f == 2:
            if a < p:
                ans += 1
                f = 1
        elif f == 3:
            if a > p:
                ans += 1
                f = 1
        elif f == 0:
            f = 1
        p = a
    else:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()