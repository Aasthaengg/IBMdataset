def main():
    X, Y = map(int, input().split())

    ans = 0
    if 1 <= X <= 3:
        ans += 100000 * (4 - X)

    if 1 <= Y <= 3:
        ans += 100000 * (4 - Y)

    if X == 1 and Y == 1:
        ans += 400000
    print(ans)

if __name__ == "__main__":
    main()