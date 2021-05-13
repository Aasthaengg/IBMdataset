def main():
    K = int(input())
    A = list(map(int, input().split()))
    mn = 2
    mx = 2
    for a in reversed(A):
        if mx < a:
            print(-1)
            return
        mn = -(-mn//a) * a
        mx = mx // a * a + (a-1)
        if mx < mn:
            print(-1)
            return
    print(mn, mx)


if __name__ == "__main__":
    main()
