import math

while True:
    n = int(input())
    if n == 0:
        break
    data = [int(n) for n in input().split()]
    ave = sum(data) / len(data)
    var = 0
    for s in data:
        var += (s - ave) ** 2
    print(math.sqrt(var / len(data)))