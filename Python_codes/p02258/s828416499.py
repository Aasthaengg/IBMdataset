n = int(input())
r_min = int(input())
r_ji = - float('inf')
for t in range(n - 1):
    r_t = float(input())
    if r_ji < r_t - r_min:
        r_ji = r_t - r_min
    if r_t < r_min:
        r_min = r_t
print(int(r_ji))
