def resolve():
    n = int(input())
    a = input()
    b = input()
    c = input()
    ans = 0
    for ai, bi, ci in zip(a, b, c):
        ans += len({ai, bi, ci}) - 1
    print(ans)


if __name__ == "__main__":
    resolve()
