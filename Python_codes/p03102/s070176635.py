def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        a = list(map(int, input().split()))
        ans = sum([a[j]*b[j] for j in range(m)]) + c
        if ans > 0:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()