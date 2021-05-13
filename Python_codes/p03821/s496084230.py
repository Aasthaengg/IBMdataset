from math import gcd
def lcm(x,y):
    return x*y//gcd(x,y)
n = int(input())
a_ls = [0] * n
b_ls = [0] * n
for i in range(n):
    a_ls[i], b_ls[i] = map(int,input().split())
add = 0
for i in range(n-1,-1,-1):
    a = a_ls[i] + add
    b = b_ls[i]
    if a % b == 0:
        continue
    else:
        diff = b - a%b
        add += diff
print(add)

