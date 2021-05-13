def main():
    N = int(input())

    if N % 2 == 0:
        ans = 1 / 2
    else:
        ans = (N // 2 + 1) / N

    print(f"{ans:.10f}")


if __name__ == "__main__":
    main()
