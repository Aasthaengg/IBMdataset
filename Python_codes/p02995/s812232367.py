import numpy as np

a,b,c,d = map(int,input().split())

cdlcm = np.lcm(c,d)

a_c = (a-1) // c
b_c = b // c
a_d = (a-1) // d
b_d = b // d
a_cd = (a-1) // (cdlcm)
b_cd = b // (cdlcm)

ans = (b-(a-1)) - (b_c - a_c) - (b_d - a_d) + (b_cd - a_cd)

print(ans)