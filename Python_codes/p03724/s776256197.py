# AGC014B - Unplanned Queries
def main():
    N, _, *A = map(int, open(0).read().split())
    T = [0] * (N + 1)
    for i in A:
        T[i] += 1
    flg = all(i % 2 == 0 for i in T)
    print("YES" if flg else "NO")


if __name__ == "__main__":
    main()