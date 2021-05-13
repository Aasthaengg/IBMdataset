n = int(input())
a = list(map(int, input().split()))

color = [0]*8
cnt = 0
free = 0

for x in a:
    tmp = x // 400
    if tmp >= 8:
        free += 1
        continue
    if color[tmp] == 0:
        color[tmp] = 1
        cnt += 1

print(max(cnt, 1), cnt + free)
