N, T = map(int, input().split())
A = list(map(int, input().split()))

max_d = 0
max_count = 0

current_min = 999999999
current_max = 0

for a in A:
    if a < current_min:
        current_min = a
        current_max = 0
        if max_d < (current_max - current_min):
            max_d = current_max - current_min
            max_count = 1
        elif max_d == (current_max - current_min):
            max_count += 1

    if a > current_max:
        current_max = a
        if max_d < (current_max - current_min):
            max_d = current_max - current_min
            max_count = 1
        elif max_d == (current_max - current_min):
            max_count += 1

print(max_count)
