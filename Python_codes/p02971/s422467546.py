n = int(input())
max_n = -1
semi_max_n = -1
max_idx = -1
for i in range(n):
    x = int(input())
    if x > max_n:
        max_n = x
        max_idx = i
    elif x >= semi_max_n:
        semi_max_n = x
for i in range(n):
    if i == max_idx:
        print(semi_max_n)
    else:
        print(max_n)