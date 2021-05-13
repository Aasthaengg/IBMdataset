n = int(input())
min_point = 0
min_rank = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > min_rank:
        min_rank = a
        min_point = b
print(min_rank+min_point)
