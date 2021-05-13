N = int(input())
i = 0
goods = []
while i < N:
    goods.append(int(input()))
    i += 1

ans = sum(goods) - max(goods) + (max(goods) // 2)
print(ans)