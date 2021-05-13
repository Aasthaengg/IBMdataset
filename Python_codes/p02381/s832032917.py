while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    m = sum(s) / n
    a = sum((x - m) ** 2 for x in s) / n
    print(a ** 0.5)