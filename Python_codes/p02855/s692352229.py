h, w, k = map(int, input().split())
ans = []
color = 0
count = 0
for i in range(h):
    line = input()
    strawberry = [i for i in range(w) if line[i] == '#']
    if not strawberry:
        count += 1
        continue
    paint = []
    now = -1
    for pos in strawberry:
        color += 1
        paint += [color] * (pos - now)
        now = pos
    paint += [color] * (w-now-1)
    ans.append(paint)
    for _ in range(count):
        ans.append(paint)
    count = 0

for i in range(count):
    ans.append(ans[-1])

for line in ans:
    print(' '.join(map(str, line)))