n = int(input())

min = float('inf')
max_diff = -float('inf')

for _ in range(n):
    i = int(input())

    if max_diff < i - min:
        max_diff = i - min

    if i < min:
        min = i

print(max_diff)