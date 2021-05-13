def count_c(li1, li2):
    c = 0
    for i in range(10):
        if li1[i] == 1 and li1[i] == li2[i]:
            c += 1
    return c


n = int(input())
open_time_list = [list(map(int, input().split())) for _ in range(n)]
profit_list = [list(map(int, input().split())) for _ in range(n)]
ans = -10000000000000000000000000000000000
# [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]総当たり
for i in range(1, 2 ** 10):
    f_list_joisino = list(map(int, list(format(i, 'b').zfill(10))))
    temp_profit = 0
    for profit_index, f_list in enumerate(open_time_list):
        temp_profit += profit_list[profit_index][count_c(
            f_list, f_list_joisino)]
    if ans < temp_profit:
        ans = temp_profit

print(ans)
