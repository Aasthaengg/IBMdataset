# https://atcoder.jp/contests/abc063/tasks/arc075_b
n, a, b = map(int, input().split())

monster = []
for i in range(n):
    monster.append(int(input()))

def damage(monster, t):
    temp = []
    for hp in monster:
        s = hp - t * b
        if s > 0:
            temp.append(s)
    ans = 0
    for hp in temp:
        if hp % (a - b) != 0:
            ans += 1
        ans += hp // (a - b)
    return True if ans <= t else False

ans = float('inf')
l = 0
r = 10 ** 9
while l <= r:
    mid = (l + r) // 2
    if damage(monster, mid):
        ans = min(ans, mid)
        r = mid - 1
    else:
        l = mid + 1
print(ans)