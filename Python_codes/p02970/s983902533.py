def main():
    N, D = (int(x) for x in input().split())
    ans = int((N + (2 * D)) / ((2 * D) + 1))
    print(ans)


if __name__ == "__main__":
    main()
