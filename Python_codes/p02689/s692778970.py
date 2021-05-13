def abc166c_peaks():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    check = [1] * n
    for i in range(m):
        a, b = map(int, input().split())
        if h[a-1] <= h[b-1]:
            check[a-1] = 0
        if h[b-1] <= h[a-1]:
            check[b-1] = 0
    print(sum(check))

abc166c_peaks()