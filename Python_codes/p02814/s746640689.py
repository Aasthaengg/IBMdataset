# x=a_i * (p+0.5)
# 前提としてaが偶数
# x= (a_i//2)*(2*p+1)
from fractions import gcd

n, m = map(int, input().split())
A = list(map(int, input().split()))
koubai = A[0] // 2
temp = koubai & -koubai
for i in range(1, n):
    a = A[i]
    if a % 2 == 1:
        print(0)
        exit()
    a //= 2
    if a & -a != temp:
        print(0)
        exit()
    g = gcd(koubai, a)
    koubai *= a // g


ans = m // koubai
if ans == 0:
    ans = 0
elif ans % 2 == 0:
    ans //= 2
else:
    ans //= 2
    ans += 1
print(ans)
