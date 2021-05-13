def main():
    n, a, b = map(int, input().split())
    ans = min(n*a, b)
    print(ans)


if __name__ == "__main__":
    main()
