import math

A, B, C, D = [int(x) for x in input().split(" ")]
lcm_c_d = (C * D) // math.gcd(C, D)
num_c = (B // C) - (A - 1) // C
num_d = (B // D) - (A - 1) // D
num_cd = (B // lcm_c_d) - (A - 1) // lcm_c_d
print(B - A - num_c - num_d + num_cd + 1)
