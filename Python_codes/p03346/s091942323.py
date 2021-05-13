def main():
    n = int(input())
    a = [-1]*(n+2)
    for i in range(1, n+1):
        x = int(input())
        a[x] = i
    x, y = 1, 1
    ans = 0
    while y < n+2:
        if a[y-1] > a[y]:
            buf = y - x
            if buf > ans:
                ans = buf
            x = y
        y += 1
    print(n - ans)

if __name__ == "__main__":
    main()