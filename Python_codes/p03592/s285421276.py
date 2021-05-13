def nm(n, m, k):
    for i in range(n+1):
        for j in range(m+1):
            black = (n - i) * j + (m - j) * i
            if black == k:
                return "Yes"
    return "No"


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    ans = nm(n, m, k)
    print(ans)
