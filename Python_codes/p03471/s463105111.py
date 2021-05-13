N, Y = map(int, input().split())

ans = [0, 0, 0]
for x in range(N+1):
    for y in range(N-x+1):
        if x * 1000 + y * 5000 + (N-x-y) * 10000 == Y:
            print(N-x-y, y, x)
            exit()
print(-1, -1, -1)
