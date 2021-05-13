def main():
    n, m = map(int, input().split())
    count = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        count[a-1] += 1
        count[b-1] += 1

    print(*count, sep="\n")


if __name__ == "__main__":
    main()
