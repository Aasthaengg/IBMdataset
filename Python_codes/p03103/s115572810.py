N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N)]

AB.sort(key=lambda x:x[0])

ret = 0
money = 0

for a, b in AB:
    if ret >= M:
        break

    while ret < M and b >= 1:
        b -= 1
        ret += 1
        money += a
        
print(money)