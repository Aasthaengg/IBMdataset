N, M = map(int, input().split())
lamp = []
for _ in range(M):
    lamp.append(list(map(int, input().split()))[1:])
P = list(map(int, input().split()))
res = 0
for bit in range(1<<N):
    on = 0
    for l in range(M):
        temp = 0
        for i in lamp[l]:
            i -= 1
            if (bit >> i) & 1 == 1:
                temp += 1
        if temp%2 == P[l]:
            on += 1
    if on == M:
        res += 1
print(res)