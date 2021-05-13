# 方針はX回で出来るかどうかの二分探索
N, A, B = map(int, input().split())
demon_health = [0 for i in range(N)]
for i in range(N):
    demon_health[i] = int(input())

high = int(1e10)
low = 0
mid = 0
ad_attack = B - A

while low < high:
    big_magic = 0
    mid = (high + low) // 2
    # mid*Bを使ってB-Aが何回必要かみたいな
    for i in range(N):
        big_magic += max((demon_health[i] - B * mid + (A - B - 1)) // (A - B), 0)
        # print(big_magic)
    if big_magic > mid:
        # cannot
        low = mid + 1
    else:
        high = mid
    # print("high, low -> " + str(high) + " " + str(low))

print(low)
