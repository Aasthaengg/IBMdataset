N, L = map(int, input().split())

curr_min = float('inf')
curr_sum = 0
for i in range(1, N + 1):
    curr_flavour = L + i - 1
    curr_sum += curr_flavour
    if curr_min >= 0:
        curr_min = min(curr_min, curr_flavour)
    else:
        curr_min = max(curr_min, curr_flavour)
print(curr_sum - curr_min)