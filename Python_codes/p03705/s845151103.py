n, a, b = map(int, input().split())

sum_min = a + a * (n - 2) + b 
sum_max = a + b * (n - 2) + b

print(max(sum_max - sum_min + 1, 0))