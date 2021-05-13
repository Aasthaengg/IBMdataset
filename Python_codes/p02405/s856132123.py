while (1):
    h, w = map(int, input().split())
    if (h == 0) and (w == 0):
        break
    a = ["#." * (w // 2) + "#" * (w % 2), ".#" * (w//2) + "." * (w % 2)]
    for i in range(h):
        print(a[i % 2])
    print()
