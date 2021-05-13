def resolve():
    a, b, c = map(int, input().split())
    ans = "Yes" if a + b >= c else "No"
    print(ans)


if __name__ == "__main__":
    resolve()
