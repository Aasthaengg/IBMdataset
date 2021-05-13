n = int(input())

a_list = list(map(int, input().split()))
a_list.sort()
a_max = a_list[n - 1]
temp_max = [1, 0]
bunbo = 1
bunshi = 1
center = int((a_max + 1) / 2)
a_set = set(a_list)
diff_min = a_max
ans = 0
for a in a_set:
    diff = abs(a-center)
    if diff_min > diff:
        diff_min = diff
        ans = a

print(a_max, ans)
