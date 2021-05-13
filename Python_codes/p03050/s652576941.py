def main():
    import sys
    import time
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    N = int(input())
    mod = N
    ans = 0
    c = 1
    while True:
        if N // mod == N % mod:
            ans += mod
            c += 1
            mod = N // c
            continue
        mod -= 1
        if not mod:
            break
        if N % mod > c:
            c += 1
            mod = N // c
            continue
        if N // mod == N // c:
            c += 1

    print(ans)

if __name__ == '__main__':
    main()