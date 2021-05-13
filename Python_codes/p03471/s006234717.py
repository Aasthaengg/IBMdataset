N, Y = map(int, input().split())
found = False
for k10 in range(N+1):
    if 10000 * k10 > Y:
        continue
    for k5 in range(N+1 - k10):
        k1 = N - k10 - k5
        if Y == 1000 * k1 + 5000 * k5 + 10000 * k10:
            found = True
            break
    if found:
        print(k10, k5, k1)
        break
else:
    print(-1, -1 ,-1)

