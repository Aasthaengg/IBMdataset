if __name__ == "__main__":
    n, m = map(int, input().split())

    if n > 3 and m > 3:
        ans = (n-2) * (m-2)
    elif n == 1 and m == 1:
        ans = 1
    elif n == 1 and m > 3:
        ans = m - 2
    elif m == 1 and n > 3:
        ans = n - 2
    else:
        ans = 0

    print(ans)
