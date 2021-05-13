def main():
    import sys
    input = sys.stdin.readline
    n, t = list(map(int, input().rstrip('\n').split()))
    T = list(map(int, input().rstrip('\n').split()))
    cnt = 0
    for i in range(1, n):
        cnt += min(T[i] - T[i-1], t)
    print(cnt + t)


if __name__ == '__main__':
    main()
