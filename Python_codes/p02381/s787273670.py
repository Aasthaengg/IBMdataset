import math

while True:
    n = int(input())
    if 0 == n:
        break

    points = list(map(int, input().split(' ')))

    m = sum(points)/n
    s = math.sqrt(sum([ (s - m)**2 for s in points ])/n)

    print('{:.5f}'.format(s))