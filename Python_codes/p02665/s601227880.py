from math import ceil

n = int(input())
a = list(map(int, input().split()))

bottom_n_list = [(0, 0) for _ in range(n + 1)]
bottom_n_list[n] = (a[n], a[n])
for i in range(n-1, -1, -1):
    leaf_num = a[i]
    min_a_node_num = ceil(bottom_n_list[i + 1][0] / 2)
    max_a_node_num = min(bottom_n_list[i + 1][1], 2 ** i - leaf_num)
    if max_a_node_num < min_a_node_num:
        print(-1)
        exit()
    bottom_n_list[i] = (min_a_node_num + leaf_num, max_a_node_num + leaf_num)

top_n_list = [0]*(n+1)
if 1 < bottom_n_list[0][0] or bottom_n_list[0][1] < 1:
    print(-1)
    exit()
top_n_list[0] = 1
ans = 1
for i in range(1, n+1):
    top_n_list[i] = min(bottom_n_list[i][1], (top_n_list[i-1]-a[i-1])*2)
    ans += top_n_list[i]

print(ans)