def main():
    x, t = map(int, input().split())
    if x < t:
        ans = 0
    else:
        ans = x - t
    print(ans)


if __name__ == "__main__":
    main()
