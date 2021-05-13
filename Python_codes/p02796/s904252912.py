n = int(input())
robo = [0] * n
for i in range(n):
    x, l = map(int, input().split())
    robo[i] = (x - l, x + l)
robo.sort(key=lambda x: x[1])

max_r, cnt = -float('inf'), 0
for l, r in robo:
    if  max_r <= l:
        cnt += 1
        max_r = r
print(cnt)