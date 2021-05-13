def main():
    n, k = int(input()), int(input())
    cnt = 0
    x = 1

    for _ in range(n):
        x *= 2
        cnt += 1
        if x > k:
            break

    print(x + k * (n - cnt))


if __name__ == "__main__":
    main()
