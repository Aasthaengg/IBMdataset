def main(n, a, b, c):
    ans = 0
    for i in range(n):
        ans += len(set([a[i], b[i], c[i]])) - 1

    print(ans)


if __name__ == "__main__":
    n = int(input())
    a = input()
    b = input()
    c = input()

    main(n, a, b, c)
