import math
while(True):
    if input() == '0':
        break
    a = list(map(int, input().split()))
    m = sum(a) / len(a)
    b = 0
    for i in a:
        b += (i - m) ** 2.0
    stddev = math.sqrt(b / len(a))
    print(stddev)
