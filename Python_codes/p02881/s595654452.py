import math

N = int(input())
min_move_count = 10**13

for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        move_count = i + (N // i) - 2
        if move_count < min_move_count:
            min_move_count = move_count

ans = min_move_count
print(ans)
