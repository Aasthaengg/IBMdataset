def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [b[0]] + b
    for i in range(n - 1):
        if max(a[i], a[i + 1]) != b[i]:
            a[i] = min(a[i], b[i])
            a[i + 1] = min(a[i + 1], b[i])
    print(sum(a))


if __name__ == '__main__':
    main()

