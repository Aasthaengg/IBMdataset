n, a, b = map(int, input().split())
if a > b:
    print(0)
elif n == 1:
    if a == b:
        print(1)
    else:
        print(0)
elif n == 2:
    print(1)
else:
    # min = a*n +b-a max = b*n + a -b までを全て取れる。
    print(1 + (b - a) * (n - 2))
