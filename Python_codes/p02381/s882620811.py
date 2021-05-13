import math
while True:
    n = int(input())
    if n == 0: break
    s = [int(e) for e in input().split()]
    average = sum(s) / n
    total = 0
    for e in s:
        total += (e - average)**2 # 偏差の２乗の合計
    print("{0: .4f}".format(math.sqrt(total/n)))

