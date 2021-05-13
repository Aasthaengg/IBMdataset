# 最高で進んでもtを超えることはできない
# 1ターンにつき1進むので偶奇をみる

n = int(input())
pre = [0, 0, 0]  # time, x, y
for i in range(n):
    t, x, y = map(int, input().split())
    t -= pre[0]
    x -= pre[1]
    y -= pre[2]
    if t < abs(x) + abs(y) or (abs(x) + abs(y)) % 2 != t % 2:
        print("No")
        exit()
    pre = [t, x, y]
print("Yes")