def solve():
    N = int(input())
    n = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        if i % 2:
            for j in range(i, N + 1, i):
                n[j] += 1
    print(n.count(8))


if __name__ == "__main__":
    solve()
