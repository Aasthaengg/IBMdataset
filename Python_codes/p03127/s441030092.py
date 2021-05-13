N = int(input())
arr = sorted(list(map(int, input().split())))

import math
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

ans_list = sorted(make_divisors(arr[0]),reverse=True)

for i in ans_list:
    flg =True
    for j in arr:
        if j%i != 0:
            flg =False
            break
    if flg:
        print(i)
        exit()