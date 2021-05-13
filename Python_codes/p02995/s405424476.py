import math


A, B, C, D = map(int, input().split())

if C == 1 or D == 1:
    print(0)
    exit()

count_all = B - A + 1
count_c = (B // C) - math.ceil(A / C) + 1
count_d = (B // D) - math.ceil(A / D) + 1
lcm_cd = C * D // math.gcd(C, D)
count_cd = (B // lcm_cd) - math.ceil(A / lcm_cd) + 1

ans = count_all - (count_c + count_d - count_cd)
print(ans)
