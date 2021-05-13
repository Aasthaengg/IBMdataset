# 066_a
a, b, c = map(int, input().split())
if (1 <= a & a <= 10000) & (1 <= b & b <= 10000) & (1 <= c & c <= 10000):
    p_ab = a + b
    p_bc = b + c
    p_ac = a + c
    print(min(p_ab,p_bc,p_ac))
