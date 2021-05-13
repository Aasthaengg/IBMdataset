def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    f = True
    ans = 0
    L = n-1
    for i in reversed(range(n)):
        if i < a[i] or a[i] < i-L:
            f = False
            break
        if i-L < a[i]:
            ans += a[i]
            L = i - a[i]
    if f:
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()