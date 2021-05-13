n = int(input())
A = map(int, input().split())

rate = set()
free = 0
for a in A:
    if a < 3200:
        rate.add(a // 400)
    else:
        free += 1

if len(rate) == 0:
    color_min, color_max = 1, n
else:
    color_min, color_max = len(rate), len(rate) + free

print(color_min, color_max)