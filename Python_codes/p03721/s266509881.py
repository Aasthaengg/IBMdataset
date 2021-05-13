N, K = map(int, input().split())
ab = [[int(i) for i in input().split()] for i in range(N)]
ab.sort()
check = 0
for a, b in ab:
    check += b
    if check >= K:
        print(a)
        break