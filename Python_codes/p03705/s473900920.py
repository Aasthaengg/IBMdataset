def main():
    import sys
    input = sys.stdin.readline
    N, A, B = [int(x) for x in input().strip().split()]
    if N == 1 and A != B:
        print(0)
        return
    elif A > B:
        print(0)
        return
    print((B * (N - 1) + A) - (B + A * (N - 1)) + 1)

if __name__ == '__main__':
    main()