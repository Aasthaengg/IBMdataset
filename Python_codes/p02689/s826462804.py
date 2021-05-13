def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    to = [0]*n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        to[a] = max(to[a], h[b])
        to[b] = max(to[b], h[a])
    ans = 0
    for hi, ti in zip(h, to):
        if hi > ti:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()