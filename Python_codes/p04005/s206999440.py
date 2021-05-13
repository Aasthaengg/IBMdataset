from statistics import median

A, B, C = [int(x) for x in input().split()]

min_num = min(A, B, C)
mid_num = median([A, B, C])
high_num = max(A, B, C)

print(min_num * mid_num * -(-high_num // 2) -
      min_num * mid_num * (high_num - -(-high_num // 2)))
