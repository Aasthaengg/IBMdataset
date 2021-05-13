def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 3**n
    ans = 0
    for i in range(x):
        p = i
        buf = 1
        for j in range(n):
            q = p%3
            if q == 0:
                buf *= a[j] - 1
            elif q == 1:
                buf *= a[j]
            else:
                buf *= a[j] + 1
            p //= 3
        if buf % 2 == 0:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
