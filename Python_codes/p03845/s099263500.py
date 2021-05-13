n = int(input())
t_list = [int(x) for x in input().split()]
t_sum = sum(t_list)
m = int(input())
for _ in range(m):
    p, x = [int(x) for x in input().split()]
    print(t_sum - t_list[p - 1] + x)