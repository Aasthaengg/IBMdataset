from math import gcd
from math import ceil
n = int(input())
T = [0] * n
A = [0] * n
for i in range(n):
    T[i], A[i] = map(int, input().split())

t, a = 1, 1
for i in range(n):
    t_rate, a_rate = T[i], A[i]
    #print(t_rate, a_rate)
    t_mul, a_mul = -(-t // t_rate), -(-a // a_rate)
    #print(t_mul, a_mul)
    mul_num = max(t_mul, a_mul)
    t, a = mul_num * t_rate, mul_num * a_rate

print(t + a)