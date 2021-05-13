import math

while True:
    n = float(input())
    aan = 0
    if n == 0:
        break
    scores = list(map(float, input().split()))
    total = sum(scores)
    avg = total / len(scores)
    for score in scores:
        aan += (score - avg)**2
    aa = aan / len(scores)
    a = math.sqrt(aa)
    print(a)
