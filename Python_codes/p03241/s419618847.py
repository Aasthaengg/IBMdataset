N, M = map(int, input().split())
from math import sqrt

def divisor(num):
    max_num = int(sqrt(num))
    divisor_list = []
    for i in range(1, max_num + 1):
        if num % i == 0:
            divisor_list.append(i)
            divisor_list.append(num//i)
    return divisor_list

g_list = divisor(M)
g_list.sort(reverse=True)
ans = 0
for g in g_list:
    if M//g >= N:
        ans = g
        break
print(ans)