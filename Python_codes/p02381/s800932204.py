while True:
    n = int(input())
    if n == 0:
        break

    s = list(map(int, input().split()))
    m = sum(s) / n
    v = 0
    for si in s:
        v += (si - m) ** 2
    ans = (v / n) ** 0.5
    print("{:.5f}".format(ans))
