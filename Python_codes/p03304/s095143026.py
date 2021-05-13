def solve(n, m, d):
    return (m - 1) * 2 * (n - d) / n**2 if d else (m - 1) / n

if __name__ == "__main__":
    n, m, d = map(int, input().split())
    print(solve(n, m, d))