while True:
    n = int(input())
    if n == 0:
        break
    m = list(map(int, input().split()))
    mean = sum(m) / len(m)
    std = (sum([(i - mean) ** 2 for i in m]) / len(m)) ** 0.5
    print("{:4f}".format(std))
