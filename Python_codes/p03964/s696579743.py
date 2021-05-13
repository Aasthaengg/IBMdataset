import math

n = int(input())
t_a = [tuple(map(int, input().split())) for _ in range(n)]

tmp_tuple = t_a[0]
ans = sum(tmp_tuple)
# ans = sum(tmp_tuple)
for i in range(1, n):
    if (tmp_tuple[0] / t_a[i][0]) == (tmp_tuple[1] / t_a[i][1]):
        continue
    else:
        # to prevent error
        factor = max(math.ceil((tmp_tuple[0] + t_a[i][0] - 1) // t_a[i][0]), math.ceil((tmp_tuple[1] + t_a[i][1] - 1) // t_a[i][1]))

    tmp_tuple = tuple(map(lambda x: x * factor, t_a[i]))
    # print(tmp_tuple)
    # print(sum(tmp_tuple) - ans)
    ans = sum(tmp_tuple)
    
print(sum(tmp_tuple))
