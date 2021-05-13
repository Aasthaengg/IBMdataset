def solve():
    X = int(input())
    ans = 1
    for b in range(1, X):
        for p in range(2, X):
            if b ** p <= X:
                ans = max(ans, b ** p)
            else:
                break
    print(ans)


if __name__ == "__main__":
    solve()
