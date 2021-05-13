def main():
    x, y = map(int, input().split())
    ans = 0
    while x <= y:
        x *= 2
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
