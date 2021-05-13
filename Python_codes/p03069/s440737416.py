def main():
    n = int(input())
    s = input()
    a = [0]*n
    b = [0]*n
    for i in range(n):
        if s[i] == "#":
            a[i] += 1
        if 0 < i:
            a[i] += a[i-1]
    for i in reversed(range(n)):
        if s[i] == ".":
            b[i] += 1
        if i < n-1:
            b[i] += b[i+1]
    ans = float("inf")
    for i in range(1, n):
        ans = min(ans, a[i-1]+b[i])
    ans = min(ans, b[0], a[n-1])
    print(ans)

if __name__ == "__main__":
    main()
