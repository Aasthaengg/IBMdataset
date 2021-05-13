"""
x = ai(p+0.5)
0.5が入っていると整数として扱いづらいので、aiが偶数であることを利用して以下のように変形
x = ai'(2p+1)
ai' = 2ai
ここで2p+1が奇数であることから、xおよびai'が2で割れる回数は同じでなければならない。
2で割れる回数をtとすると、
x' = ai''(2p+1)
x' = x/(2^t)
ai'' = ai'/(2^t)
Mも2^tで割っておく。
M' = M/(2^t)
Xとして何が考えられるかは、まずai''の最小公倍数Lが考えられる
lcm(ai'') = L
さらに、Lの奇数倍も考えられる
したがって答えは、M'/2Lの小数点以下切り上げたもの
"""

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

def func(x):
    """2で何回割れるか"""
    res = 0
    while x%2 == 0:
        x //= 2
        res += 1
    return res

#from math import gcd # v3.5以降
from fractions import gcd # v3.4以前
from functools import reduce

def lcm_base(x, y):
    """2つの値の最小公倍数"""
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    """3つ以上の値の最小公倍数"""
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    """3つ以上の値の最小公倍数"""
    return reduce(lcm_base, numbers, 1)

def main(n,m,a):
    ans = 0
    # a -> a'
    for i in range(n):
        if a[i]%2 == 1:
            print(0)
            return
        a[i] //= 2

    # a' -> a''
    t = func(a[0])
    for i in range(n):
        if func(a[i]) != t:
            print(0)
            return
        a[i] >>= t # a[i] //= 2^t
    m >>= t

    l = 1
    for i in range(n):
        l = lcm(l, a[i])
        if l > m:
            print(0)
            return

    m //= l
    ans += (m+1)//2
    print(ans)
    
main(n,m,a)