import math

k = int(input())
k_range = range(1, k + 1)

sum_gcd = 0
for l in k_range:
    temp = 0
    for m in k_range:
        temp = math.gcd(l, m)
        for n in k_range:
            sum_gcd += math.gcd(n, temp)

print(sum_gcd)