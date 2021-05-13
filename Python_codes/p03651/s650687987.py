n,k = list(map(int, input().split()))
a = sorted(list(map(int, input().split())), reverse=True)

# 作れない数字
# ・最大値より大きい数字
# ・GCDの倍数でない数字

if k > a[0]:
    print('IMPOSSIBLE')
    exit()

import math

gcd = a[0]
for i in a:
    gcd = math.gcd(gcd, i)
    if k%gcd == 0:
        print('POSSIBLE')
        exit()
    
print('IMPOSSIBLE')
