from bisect import bisect_left

a, b, q = [int(i) for i in input().split()]

s_list = [int(input()) for _ in range(a)]
t_list = [int(input()) for _ in range(b)]

for _ in range(q):
    x = int(input())

    temp_s_t_list = [10 ** 11] * 4
    
    si = bisect_left(s_list, x)
    if si < a:
        temp_s_t_list[0] = s_list[si] - x
    if si > 0:
        temp_s_t_list[1] = s_list[si - 1] - x
    
    ti = bisect_left(t_list, x)
    if ti < b:
        temp_s_t_list[2] = t_list[ti] - x
    if ti > 0:
        temp_s_t_list[3] = t_list[ti - 1] - x

    ans = 10 ** 11 * 3
    for s_x, t_x in [(temp_s_t_list[0], temp_s_t_list[2]), (temp_s_t_list[0], temp_s_t_list[3]), (temp_s_t_list[1], temp_s_t_list[2]), (temp_s_t_list[1], temp_s_t_list[3])]:
        temp_s_x = s_x
        s_x = abs(s_x)
        temp_t_x = t_x
        t_x = abs(t_x)
        if temp_s_x // s_x == temp_t_x // t_x:
            temp = max(s_x, t_x)
        else:
            temp = s_x + t_x + min(s_x, t_x)

        if ans > temp:
            ans = temp
    print(ans)