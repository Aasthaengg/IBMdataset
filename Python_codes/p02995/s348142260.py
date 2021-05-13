import math

a, b, c, d = map(int, input().split())
total = b - a + 1
c_cnt = b // c - (a-1) // c
d_cnt = b // d - (a-1) // d
common_div = (c * d) // math.gcd(c, d)
common_cnt = b // common_div - (a-1) // common_div
total = total - c_cnt - d_cnt + common_cnt
print(total)
