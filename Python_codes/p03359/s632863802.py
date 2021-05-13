def resolve():
    a, b = map(int, input().split())
    date = 100 * a + b
    cand = [100 * i + i for i in range(1, 13)]
    print(len([c for c in cand if c <= date]))


if __name__ == "__main__":
    resolve()
