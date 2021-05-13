import math
while 1:
    N = int(input())
    if N == 0:
        break
    xs = list(map(int, input().split()))
    avg = 0
    for x in xs:
        avg += x
    avg /= len(xs)
    var = 0
    for x in xs:
        var += (x - avg) ** 2
    var /= len(xs)
    print(math.sqrt(var))
