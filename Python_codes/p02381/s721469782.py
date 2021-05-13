import math

while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    m = sum(s) / n
    ss = 0
    for i in s:
        ss += pow((i - m), 2)
    bun = ss / n
    print(math.sqrt(bun))
