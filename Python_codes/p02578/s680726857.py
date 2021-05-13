N = int(input())
A = [int(x) for x in input().split()]
maxBefore = 0
steps = 0

for x in A:
    if x < maxBefore:
        steps += maxBefore - x
    else:
        maxBefore = x
print(steps)