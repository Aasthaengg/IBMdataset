def main():
    n, k = map(int, input().split())
    As = list(map(int, input().split()))

    ans = (n-2) // (k-1) + 1
    print(ans)


if __name__ == "__main__":
    main()
