# 最大公約数：ユークリッドの互除法
import sys

def gcd(x, y):
    return y if not x%y else gcd(y, x%y)

def get_input():
    data = []
    for line in sys.stdin:
        a, b = [int(i) for i in line.split()]
        data.append((a,b))
    return data


data = get_input()

for x,y in data:
    GCD = gcd(x,y)
    LCM = x*y // GCD
    print(GCD, LCM)
