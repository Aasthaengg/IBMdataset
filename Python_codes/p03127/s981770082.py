import math
n = int(input())
l = list(map(int, input().split()))
def multiGCD(l):
    ans = 0
    for i in l:
        ans = math.gcd(ans, i)
    return ans
print(multiGCD(l))