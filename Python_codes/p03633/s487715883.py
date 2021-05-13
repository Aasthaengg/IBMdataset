from fractions import gcd

n = int(input())
t = [int(input()) for _ in range(n)]
result = 1


for i in range(n):
    num = t[i]
    result = result * num // gcd(result, num)

print(result)