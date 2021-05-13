import math

x, y = [int(i) for i in input().split()]

ans = 0

while (x <= y):
    x *= 2
    ans += 1

print(ans)