def hotel():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    first = x * k
    later = y * (n - k)
    if k > n:
        first = x * n
        later = 0
    print(first + later)

hotel()
