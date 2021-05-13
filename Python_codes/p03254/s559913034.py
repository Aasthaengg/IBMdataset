N, x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

a.sort()

cnt = 0
for i, child in enumerate(a):
    if x == 0:
        break
    if child == x:
        cnt += 1
        break
    if child < x:
        # 最後の要素か判定
        if i == len(a) - 1:
            break
        x -= child
        cnt += 1

print(cnt)