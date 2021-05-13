n = int(input())
p_list = sorted([int(input()) for _ in range(n)])
print(sum(p_list) - p_list[-1] // 2)