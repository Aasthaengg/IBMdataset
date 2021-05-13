if __name__ == "__main__":
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)

    if a[0] > x:
        a[0] = x

    for i in range(0, n-1):
        if a[i] + a[i+1] > x:
            a[i+1] = x - a[i]

    print(total-sum(a))
