def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i] - b[i] for i in range(n)]
    c.sort()
    ans = 0
    x = 0
    for v in c:
        if v < 0:
            ans += 1
            x -= v
    y = 0
    for v in reversed(c):
        if y >= x:
            break
        if v > 0:
            ans += 1
            y += v
    if y >= x:
        print(ans)
    else:
        print("-1")

if __name__ == "__main__":
    main()