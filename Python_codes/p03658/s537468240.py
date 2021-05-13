def main():
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))
    ans = sum(sorted(ls)[::-1][:k])
    print(ans)


if __name__ == "__main__":
    main()
