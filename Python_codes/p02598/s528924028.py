import math

n,k = list(map(int,input().split()))

a = list(map(int,input().split()))

middle = math.ceil(max(a) / 2)
oldMiddle = 0
h = middle // 2
rightMin = max(a)

while h > 0:
    cut = 0
    if middle == 0:
        middle = 1
        break
    for i in range(n):
        cut += math.ceil(a[i] / middle) - 1
    h = math.ceil(abs(middle - oldMiddle) / 2)
    oldMiddle = middle
    if cut <= k:
        if (middle - h == rightMin):
            break
        middle -= h
    else:
        rightMin = middle
        middle += h

print(middle)