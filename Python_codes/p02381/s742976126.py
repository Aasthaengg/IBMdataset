import math


while True:
    n = int(input())
    if n == 0:
        break
    *A, = map(int, input().split())
    m = sum(A) / n
    s2 = sum((a - m) ** 2 for a in A) / n
    print("{:.8f}".format(math.sqrt(s2)))

