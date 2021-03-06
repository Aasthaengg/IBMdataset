import math
import fractions
from functools import reduce

n, m = map(int,input().split())
a = list(map(int,input().split()))
a = [t // 2 for t in a]#リストの要素すべてを2で割る

def lcm_base(x, y):
    return (x * y)//fractions.gcd(x,y)

def lcm_list(numbers): #最小公倍数を求める
    return reduce(lcm_base, numbers, 1)

def num_dev2(x):
    return bin(x)[::-1].find("1") #２で割り切れる回数を確認

lcm = lcm_list(a)
q = m//lcm #mは最小公倍数で何回割れるか

count = 0
dev2 = num_dev2(a[0])
for i in range(1,n):
    if dev2 != num_dev2(a[i]):#リストのすべての要素の２で割れる回数は等しいか
        count += 1
        break
if count != 0:
    print(0)
else:
    print(math.ceil(q/2))