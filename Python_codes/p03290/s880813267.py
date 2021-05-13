d, g = map(int, input().split())
pc = [tuple(map(int, input().split())) for _ in range(d)]

ans = 10 ** 18
import itertools
for i in itertools.product([0, 1], repeat=d):
    point = 0
    num = 0
    # ボーナス加算
    for j in range(d):
        if i[j] == 1:
            num += pc[j][0]
            point += pc[j][1] + 100 * (j+1) * pc[j][0]
    #print('-b-', i, g, point, num)
    # 足りない分を後ろから全問-1問まで加算
    for j in reversed(range(d)):
        if g <= point:
            break
        if i[j] == 0:
            c = (g - point) // (100 * (j+1))
            if c < pc[j][0]:
                num += c
                point += 100 * (j+1) * c
            else:
                num += pc[j][0] - 1
                point += 100 * (j+1) * (pc[j][0] - 1)
        #print(i,j, g, point, num)
    #print('---', ans, num, point)
    if g <= point:
        ans = min(ans, num)
print(ans)



