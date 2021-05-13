N, K = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(N)]
AB.sort()

bsum = 0
for (a, b) in AB:
    bsum += b
    if K <= bsum:
        print(a)
        break