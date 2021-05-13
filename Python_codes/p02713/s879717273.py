import math
#from functools import reduce

#def gcd(*numbers):
#    return reduce(math.gcd, numbers)

def main():
    K = int(input())
    ans = 0
    #全てが同じ数字
    for i in range(1,K+1,1):
        for j in range(1,K+1,1):
            for k in range(1,K+1,1):
                ans += math.gcd(i,math.gcd(j,k))

    return ans

print(main())
