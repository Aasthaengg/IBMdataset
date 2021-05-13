import math

while True:
    temp = []
    n = int(input())
    if n == 0:
        break
    point = list(map(int, input().split()))
    m = sum(point)/len(point)
    for i in point:
        temp.append((i - m)**2)
    print('{0:.8f}'.format(math.sqrt(sum(temp)/n)))