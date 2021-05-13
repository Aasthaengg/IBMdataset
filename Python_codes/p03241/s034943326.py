### ABC112D Partition Diff:

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

div = divisor(M)
div.sort(reverse=True)
ans = None
for g in div:
    if N > M//g:
        continue
    ans = g
    break
print(ans)