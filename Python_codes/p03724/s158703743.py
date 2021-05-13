def main():
    n, m = map(int, input().split())
    a = [0]*(n+1)
    for _ in range(m):
        x, y = map(int, input().split())
        a[x] += 1
        a[y] += 1
    f = True
    for i in range(n+1):
        if a[i] % 2 == 1:
            f = False
            break
    if f:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()