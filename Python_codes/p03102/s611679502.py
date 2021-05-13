def main():
    n, m, c = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    sourcecode = [[int(i) for i in input().split()] for _ in range(n)]
    ans = 0
    for A in sourcecode:
        _sum = 0
        for i in range(m):
            _sum += A[i] * B[i]
        if _sum > -c:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
