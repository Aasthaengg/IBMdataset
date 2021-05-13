def main():
    n = int(input())
    a = list(map(int, input().split()))
    f = [True]*n
    ans = 0
    for i in range(n):
        if f[i]:
            f[i] = False
            if a[a[i]-1]-1 == i:
                ans += 1
                f[a[i]-1] = False
    print(ans)

if __name__ == "__main__":
    main()
