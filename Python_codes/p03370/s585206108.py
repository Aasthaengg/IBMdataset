n, x = map(int, input().split())
m  = [int(input()) for _ in range(n)]

min_m = min(m)
sum_m = 0

for i in m:
    sum_m += i

rem_x = x - sum_m

b = rem_x // min_m

print(b + len(m))