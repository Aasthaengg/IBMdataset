n = int(input())
a = list(map(int, input().split()))

cnt = 0
color = [False] * 8
for v in a:
    if v >= 3200:
        cnt += 1
    else:
        color[v//400] = True

num = color.count(True)
print(max(num, 1), num + cnt)