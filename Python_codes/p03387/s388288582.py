arr = list(map(int, input().split()))

arr.sort()

a, b, c = arr

k = (c - a) + (c - b)

if k % 2 == 0:
    print(k // 2)
else:
    print(k // 2 + 2)
