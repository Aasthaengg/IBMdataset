h1, m1, h2, m2, k = map(int, input().split())

start_mins = h1 * 60 + m1
end_min = h2 * 60 + m2

is_up = end_min - start_mins
can_start = is_up - k
print(can_start)