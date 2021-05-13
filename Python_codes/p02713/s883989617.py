import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def main():
    K = int(input())
    ans = 0
    #全てが同じ数字
    for i in range(1,K+1,1):
        ans += gcd(i,i,i)
    #2つ同じ数字
    tmp = 0
    for i in range(1,K+1,1):
        for j in range(1,K+1,1):
            if j != i:
                tmp += gcd(i,i,j)
    ans += tmp*3
    #3つの異なる数字
    tmp2 = 0
    for i in range(1,K+1,1):
        for j in range(i+1,K+1,1):
            for h in range(j+1,K+1,1):
                tmp2 += gcd(i,j,h)

    ans += tmp2*6

    return ans

print(main())
