from fractions import gcd
from functools import reduce

# 2つの数の最小公倍数
def lcm(x,y):
    return (x*y) // gcd(x,y)

# リストを引数にして最小公倍数を表示
def lcm_of_list(a):
    return reduce(lcm, a)

def waruni(a):
    return a//2


n,m = map(int, input().split())
b = list(map(waruni, map(int, input().split())))

L = lcm_of_list(b)

for i in range(n):
    if (L//b[i])%2==0:
        print(0)
        exit()

ans = (m//L+1)//2

print(ans)