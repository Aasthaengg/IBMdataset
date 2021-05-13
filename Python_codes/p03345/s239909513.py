def resolve():
    a, b, c, k = map(int, input().split())
    ans = b - a if k % 2 else a - b
    if abs(ans) > 10 ** 18:
        print("Unfair")
    else:
        print(ans)


if __name__ == "__main__":
    resolve()
