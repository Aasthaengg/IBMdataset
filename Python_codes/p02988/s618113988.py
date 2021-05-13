def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, n - 1):
        a = [p[i - 1], p[i], p[i + 1]]
        if p[i] != max(a) and p[i] != min(a):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
