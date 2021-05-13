def f(a, d):
    b = 1
    cnt = 1
    while True:
        b += a
        if d < b:
            break
        cnt += 1

    return cnt


def main():
    n = int(input())
    d, x = map(int, input().split())
    ans = 0

    for _ in range(n):
        a = int(input())
        ans += f(a, d)

    print(ans + x)


if __name__ == "__main__":
    main()
