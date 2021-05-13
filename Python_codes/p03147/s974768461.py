N = int(input())
h = list(map(int,input().split()))

count = 0
while h.count(0) != N:
    beforeWater = False
    for i in range(N):
        if h[i] > 0:
            if not beforeWater:
                count += 1
            h[i] = h[i] - 1
            beforeWater = True
        else:
            beforeWater = False

print(count)