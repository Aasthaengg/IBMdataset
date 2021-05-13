def main():
    n = int(input())
    a = input()
    b = input()
    c = input()
    ans = 0

    for i in range(n):
        if a[i] == b[i] and b[i] == c[i]:
            continue
        elif a[i] == b[i] and b[i] != c[i]:
            ans += 1
        elif b[i] == c[i] and c[i] != a[i]:
            ans += 1
        elif c[i] == a[i] and a[i] != b[i]:
            ans += 1
        else:
            ans += 2

    print(ans)


if __name__ == "__main__":
    main()
