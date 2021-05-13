if __name__ == "__main__":
    n, m, d = map(int, input().split())
    print((2 if d else 1) * (n - d) * (m - 1) / (n * n))
