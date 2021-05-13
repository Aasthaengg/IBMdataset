N = int(input())

A = list(map(int, input().split()))

A.sort()

minimum, maximum = A[0], A[-1]
xy = []

for i in range(1,N-1):
    num = A[i]
    if num >= 0:
        xy.append((minimum, num))
        minimum -= num
    else:
        xy.append((maximum, num))
        maximum -= num

xy.append((maximum, minimum))
print(maximum-minimum)
for x, y in xy:
    print(x,y)

