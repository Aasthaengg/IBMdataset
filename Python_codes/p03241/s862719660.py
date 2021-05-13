import math
N, M = map(int, input().split())

# M = a x bの形に分解する
pair = []
for i in range(1, int(math.sqrt(M))+1):
    if M % i == 0:
        pair.append((i, M // i))

ans = 1
for a, b in pair:
    if b >= N:
        ans = max(ans, a)
    if a >= N:
        ans = max(ans, b)

print(ans)
