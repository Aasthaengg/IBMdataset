from math import sqrt
from statistics import mean

while True:
    s = input()
    if s == "0":
        break

    l = list(map(int, input().split()))
    length = len(l)
    m = mean(l)
    print("{:.8f}".format(sqrt(sum(map(lambda i: (i-m) ** 2, l)) / length)))