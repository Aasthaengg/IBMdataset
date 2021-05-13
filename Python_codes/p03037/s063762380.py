n, m = map(int, input().strip().split())

max_left = 0
min_right = n
for _ in range(m):
    l_tmp, r_tmp = map(int, input().strip().split())
    if max_left < l_tmp:
        max_left = l_tmp
    if r_tmp < min_right:
        min_right = r_tmp

if min_right < max_left:
    print(0)
else:
    print(min_right - max_left + 1)
