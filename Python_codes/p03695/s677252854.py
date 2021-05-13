n = int(input())
a = map(int, input().split())

color_set = set()
color_free_num = 0
for a_i in a:
    if a_i >= 3200:
        color_free_num += 1
    else:
        color_set.add(a_i // 400)

ans_min = max(len(color_set), 1)
ans_max = len(color_set) + color_free_num
ans = "{} {}".format(ans_min, ans_max)
print(ans)