# 1%
import math
X = int(input())
d = []
money = 100
rate = 0.01
ans = 0
while money < X:
    money += money // 100
    ans += 1
print(ans)
