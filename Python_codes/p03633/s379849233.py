import math

num = 1
for i in range(int(input())):
    a = int(input())
    cnt = math.gcd(a, num)
    num = (a * num) // cnt
print(num)