def main():
    a, b, c, d = map(int, input().split())
    ans = max(a*b, c*d)
    print(ans)


if __name__ == "__main__":
    main()
