def main():
    n, c, k = list(map(int, input().split()))
    T = [int(input()) for _ in range(n)]
    T.sort()
    count = 0
    ans = 1
    t0 = T[0]
    for t in T:
        if t - t0 <= k:
            count += 1
        if count > c or t - t0 > k:
            ans += 1
            count = 1
            t0 = t
    print(ans)

if __name__ == '__main__':
    main()
