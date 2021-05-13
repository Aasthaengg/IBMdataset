# int(input()) # 入力が1つ
from math import ceil
n, a, b = map(int, input().split()) # 入力が複数
# [int(i) for i in input().split()] # 配列で数字

monster = []
for i in range(n):
    monster.append(int(input()))

def check(monster, t):
    temp = []
    for i in range(n):
        temp.append(monster[i] - b * t) 
    ans = 0
    for i in range(n):
        if temp[i] > 0:
            ans += ceil(temp[i] / (a - b))
    if ans <= t:
        return True
    return False

l = 0
r = 10 ** 10
ans = 10 ** 10
while l <= r:
    mid = (l + r) // 2
    if check(monster, mid):
        ans = min(ans, mid)
        r = mid - 1
    else:
        l = mid + 1
print(ans)