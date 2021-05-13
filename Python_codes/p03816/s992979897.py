import math

n = int(input())
a = [int(_) for _ in input().split()]

CARD = 10**5+1

num = [0] * CARD
for i in a:
    num[i] += 1

ans = 0
cnt = 0
for i in range(CARD):
    while num[i] > 2:
        ans += 2
        num[i] -= 2
    if num[i] == 2:
        cnt += 1
ans += math.ceil(cnt/2) * 2
print(n-ans)