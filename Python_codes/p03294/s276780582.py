import math

n = int(input())
a = list(map(int, input().split()))
common_num = 1
for num in a:
    common_num = (common_num * num) // math.gcd(common_num, num)
total = 0
for num in a:
    total += (common_num - 1) % num
print(total)
