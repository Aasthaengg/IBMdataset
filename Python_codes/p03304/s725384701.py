def main():
    n, m, d = map(int, input().split())
    ans = (m-1)
    if d == 0:
        ans /= n
    else:
        ans *= (n-d) / n / n * 2
    print(ans)


if __name__ == "__main__":
    main()
