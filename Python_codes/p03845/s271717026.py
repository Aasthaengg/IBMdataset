from copy import copy

n = int(input())
t_list = list(map(int, input().split()))
m = int(input())
px_list = [list(map(int, input().split())) for _ in range(m)]

for px in px_list:
    p, x = px
    tmp_list = copy(t_list)
    tmp_list[p - 1] = x
    print(sum(tmp_list))
